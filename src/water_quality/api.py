from contextlib import asynccontextmanager
from pathlib import Path

import pandas as pd
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field

from .config import DATA_PATH, MODEL_PATH, PROJECT_ROOT
from .pipeline import load_model, save_model, train_and_evaluate

FEATURES = [
    "ph", "Hardness", "Solids", "Chloramines", "Sulfate",
    "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity",
]


class WaterSample(BaseModel):
    ph: float = Field(..., ge=0, le=14)
    Hardness: float = Field(..., ge=0, le=500)
    Solids: float = Field(..., ge=0, le=50000)
    Chloramines: float = Field(..., ge=0, le=20)
    Sulfate: float = Field(..., ge=0, le=1000)
    Conductivity: float = Field(..., ge=0, le=2000)
    Organic_carbon: float = Field(..., ge=0, le=100)
    Trihalomethanes: float = Field(..., ge=0, le=300)
    Turbidity: float = Field(..., ge=0, le=20)


class RetrainParams(BaseModel):
    n_estimators: int = Field(300, ge=10, le=2000)
    max_depth: int | None = Field(None, ge=1, le=100)
    random_state: int = 42


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.model = None
    if MODEL_PATH.exists():
        app.state.model = load_model(MODEL_PATH)
    yield


app = FastAPI(
    title="Water Quality MLOps API",
    description="Predict water potability and retrain a tracked Random Forest model.",
    version="2.0.0",
    lifespan=lifespan,
)


@app.get("/health")
def health(request: Request):
    return {"status": "healthy", "model_loaded": request.app.state.model is not None}


@app.get("/")
def root():
    return {"message": "Water Quality MLOps API", "docs": "/docs", "ui": "/ui"}


@app.post("/predict")
def predict_potability(sample: WaterSample, request: Request):
    model = request.app.state.model
    if model is None:
        raise HTTPException(503, "No model is loaded. Call POST /retrain first.")

    frame = pd.DataFrame([[getattr(sample, name) for name in FEATURES]], columns=FEATURES)
    prediction = int(model.predict(frame)[0])
    probability = None
    if hasattr(model, "predict_proba"):
        probability = float(model.predict_proba(frame)[0][prediction])

    return {
        "prediction": prediction,
        "label": "potable" if prediction == 1 else "not potable",
        "confidence": probability,
    }


@app.post("/retrain")
def retrain_model(params: RetrainParams, request: Request):
    try:
        model, accuracy, _, _ = train_and_evaluate(
            DATA_PATH,
            n_estimators=params.n_estimators,
            max_depth=params.max_depth,
            random_state=params.random_state,
        )
        save_model(model, MODEL_PATH)
        request.app.state.model = model
        return {
            "status": "success",
            "test_accuracy": accuracy,
            "parameters_used": params.model_dump(),
        }
    except Exception as exc:
        raise HTTPException(500, f"Retraining failed: {exc}") from exc


@app.get("/ui", response_class=FileResponse)
def get_ui():
    return FileResponse(Path(PROJECT_ROOT) / "web" / "index.html")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_: Request, exc: RequestValidationError):
    errors = [{"field": error["loc"][-1], "message": error["msg"]} for error in exc.errors()]
    return JSONResponse(status_code=422, content={"errors": errors})
