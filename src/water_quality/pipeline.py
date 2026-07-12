from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

from .config import MLFLOW_TRACKING_URI
from .monitoring import log_metric

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
mlflow.set_experiment("WaterPotability")


def prepare_data(csv_path: str | Path, test_size: float = 0.2, random_state: int = 42):
    """Load, clean, impute and split the water-potability dataset."""
    frame = pd.read_csv(csv_path)
    frame["ph"] = frame["ph"].replace(0, np.nan)
    frame[frame.columns] = SimpleImputer(strategy="median").fit_transform(frame)
    features = frame.drop(columns="Potability")
    target = frame["Potability"].astype(int)
    return train_test_split(
        features,
        target,
        test_size=test_size,
        random_state=random_state,
        stratify=target,
    )


def train_and_evaluate(
    csv_path: str | Path,
    n_estimators: int = 300,
    max_depth: int | None = None,
    random_state: int = 42,
):
    """Train a Random Forest and track parameters, metrics and model in MLflow."""
    X_train, X_test, y_train, y_test = prepare_data(csv_path, random_state=random_state)

    with mlflow.start_run() as run:
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=random_state,
            class_weight="balanced",
        )
        model.fit(X_train, y_train)

        train_accuracy = accuracy_score(y_train, model.predict(X_train))
        predictions = model.predict(X_test)
        test_accuracy = accuracy_score(y_test, predictions)

        mlflow.log_params(
            {
                "n_estimators": n_estimators,
                "max_depth": max_depth,
                "random_state": random_state,
            }
        )
        mlflow.log_metrics(
            {"train_accuracy": train_accuracy, "test_accuracy": test_accuracy}
        )
        mlflow.sklearn.log_model(model, name="model", input_example=X_train.iloc[:5])
        log_metric(run.info.run_id, "test_accuracy", test_accuracy)

    report = classification_report(y_test, predictions, output_dict=True)
    return model, test_accuracy, report, (X_test, y_test)


def save_model(model, path: str | Path) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, destination)
    return destination


def load_model(path: str | Path):
    source = Path(path)
    if not source.exists():
        raise FileNotFoundError(f"Model not found: {source}")
    return joblib.load(source)
