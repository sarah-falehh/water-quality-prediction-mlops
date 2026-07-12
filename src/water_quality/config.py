from pathlib import Path
import os

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = Path(os.getenv("DATA_PATH", PROJECT_ROOT / "data" / "water_potability.csv"))
MODEL_PATH = Path(os.getenv("MODEL_PATH", PROJECT_ROOT / "artifacts" / "rf_model.joblib"))
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", f"sqlite:///{PROJECT_ROOT / 'mlflow.db'}")
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
