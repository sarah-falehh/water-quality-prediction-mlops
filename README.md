<p align="center">
  <img
    src="assets/banner.png"
    alt="Water Quality Prediction MLOps Pipeline banner"
    width="100%"
  >
</p>

<h1 align="center">
  Water Quality Prediction — End-to-End MLOps Pipeline
</h1>

<p align="center">
  <strong>
    ML engineering project covering training, evaluation, API serving,
    experiment tracking, containerization, CI, testing and monitoring.
  </strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/MLflow-Experiment_Tracking-0194E2?logo=mlflow&logoColor=white" alt="MLflow">
  <img src="https://img.shields.io/badge/Elasticsearch-Metrics-005571?logo=elasticsearch&logoColor=white" alt="Elasticsearch">
  <img src="https://img.shields.io/badge/Kibana-Visualization-E8478B?logo=kibana&logoColor=white" alt="Kibana">
  <img src="https://img.shields.io/badge/License-MIT-success" alt="MIT License">
</p>

<p align="center">
  <a href="https://github.com/sarah-falehh/water-quality-prediction-mlops/actions/workflows/mlops-ci.yml">
    <img
      src="https://github.com/sarah-falehh/water-quality-prediction-mlops/actions/workflows/mlops-ci.yml/badge.svg"
      alt="MLOps CI Pipeline"
    >
  </a>
</p>

---

## Overview

This repository demonstrates an end-to-end **MLOps workflow** for a binary
water-potability classification problem.

The project is intentionally presented primarily as an **ML engineering project**,
not as a high-performing predictive model.

It covers:

- data preprocessing;
- missing-value handling;
- stratified train/test splitting;
- Random Forest training;
- model evaluation;
- MLflow experiment tracking;
- model serialization;
- FastAPI model serving;
- Pydantic input validation;
- model retraining through an API endpoint;
- Docker containerization;
- Docker Compose orchestration;
- GitHub Actions continuous integration;
- automated testing;
- Elasticsearch metric logging;
- Kibana visualization;
- Filebeat container-log forwarding.

> [!IMPORTANT]
> The current Random Forest model shows significant overfitting.
>
> The main value of this repository is therefore the **engineering lifecycle
> around the model**, rather than the predictive performance itself.

---

## Why This Project Matters

A machine-learning model is only one component of an ML system.

A complete workflow also requires:

```text
Data
  ↓
Preprocessing
  ↓
Training
  ↓
Evaluation
  ↓
Experiment Tracking
  ↓
Model Artifact
  ↓
API Serving
  ↓
Containerization
  ↓
Automated Testing / CI
  ↓
Monitoring
```

This project was built to explore that complete lifecycle.

---

## Architecture

<p align="center">
  <img
    src="docs/architecture.png"
    alt="Water Quality MLOps architecture"
    width="95%"
  >
</p>

### High-Level Workflow

```text
Water Quality Dataset
        │
        ▼
Data Loading
        │
        ▼
Preprocessing
        │
        ▼
Train / Test Split
        │
        ▼
Random Forest Training
        │
        ├──────────► MLflow
        │             ├── Parameters
        │             ├── Metrics
        │             └── Model Artifact
        │
        └──────────► Elasticsearch
                      └── Evaluation Metric
        │
        ▼
Model Serialization
        │
        ▼
FastAPI
        │
        ├── GET  /health
        ├── POST /predict
        ├── POST /retrain
        ├── GET  /docs
        └── GET  /redoc
        │
        ▼
Docker / Docker Compose
        │
        ▼
Elasticsearch + Kibana + Filebeat
```

---

## Technology Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Data Processing | Pandas, NumPy |
| Machine Learning | Scikit-learn, Random Forest |
| Missing-Value Handling | `SimpleImputer` |
| Model Evaluation | Accuracy, Precision, Recall, F1 |
| API | FastAPI |
| Validation | Pydantic |
| Serving | Uvicorn |
| Experiment Tracking | MLflow |
| Serialization | Joblib |
| Containers | Docker, Docker Compose |
| Metrics | Elasticsearch |
| Visualization | Kibana |
| Logs | Filebeat |
| Testing | Pytest |
| CI | GitHub Actions |
| Code Quality | Black, Flake8, Bandit |

---

## Dataset

The project uses the **Water Potability** dataset.

### Dataset Summary

| Property | Value |
|---|---:|
| Observations | 3,276 |
| Total columns | 10 |
| Input features | 9 |
| Target | `Potability` |
| Non-potable samples | 1,998 |
| Potable samples | 1,278 |
| Non-potable proportion | 60.99% |
| Potable proportion | 39.01% |

### Input Features

- `ph`
- `Hardness`
- `Solids`
- `Chloramines`
- `Sulfate`
- `Conductivity`
- `Organic_carbon`
- `Trihalomethanes`
- `Turbidity`

### Missing Values

The raw dataset contains missing values in:

| Feature | Missing values |
|---|---:|
| `ph` | 491 |
| `Sulfate` | 781 |
| `Trihalomethanes` | 162 |

The implemented pipeline applies median-based imputation before model training.

The data is then split into training and test sets using an **80/20 stratified split**.

> [!NOTE]
> This repository is intended for educational and engineering purposes.
> It must not be used for real-world drinking-water safety decisions.

---

## Model

The current baseline model is:

```python
RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    random_state=42,
    class_weight="balanced",
)
```

The objective of the project is not to claim state-of-the-art predictive
performance, but to expose the full ML lifecycle around a reproducible baseline.

---

## Model Evaluation

The current evaluation clearly shows an important limitation.

### Overall Metrics

| Metric | Result |
|---|---:|
| Training accuracy | **1.0000** |
| Test accuracy | **0.6677** |
| Macro precision | 0.6723 |
| Macro recall | 0.5981 |
| Macro F1 | 0.5842 |
| Weighted precision | 0.6708 |
| Weighted recall | 0.6677 |
| Weighted F1 | 0.6251 |

### Per-Class Results

| Class | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Non-potable (`0`) | 0.6655 | **0.9150** | 0.7705 | 400 |
| Potable (`1`) | 0.6792 | **0.2812** | 0.3978 | 256 |

### Confusion Matrix

|  | Predicted non-potable | Predicted potable |
|---|---:|---:|
| Actual non-potable | 366 | 34 |
| Actual potable | 184 | 72 |

---

## What the Results Mean

The difference between:

```text
Training accuracy = 100%
Test accuracy     ≈ 66.8%
```

is a strong indication that the Random Forest is **overfitting**.

The model also behaves very differently across classes.

For non-potable water:

```text
Recall class 0 = 91.5%
```

For potable water:

```text
Recall class 1 = 28.1%
```

This means that many potable samples are incorrectly predicted as non-potable.

Therefore:

> **This model should not be presented as a strong predictive result.**

The project is more useful for demonstrating:

- ML pipeline design;
- model serving;
- API engineering;
- experiment tracking;
- reproducibility;
- testing;
- containerization;
- CI;
- monitoring.

Possible modelling improvements include:

- cross-validation;
- hyperparameter optimization;
- probability-threshold tuning;
- calibration;
- feature selection;
- resampling strategies;
- shallower trees;
- alternative classifiers;
- ensemble comparison.

---

## MLflow Experiment Tracking

MLflow is used to track model experiments.

The experiment name is:

```text
WaterPotability
```

The default backend is:

```text
sqlite:///mlflow.db
```

Each run logs:

### Parameters

- `n_estimators`
- `max_depth`
- `random_state`

### Metrics

- `train_accuracy`
- `test_accuracy`

### Artifacts

- trained Scikit-learn model;
- input example.

Start the MLflow interface with:

```bash
mlflow ui \
  --backend-store-uri sqlite:///mlflow.db \
  --host 0.0.0.0 \
  --port 5000
```

On Windows PowerShell:

```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 5000
```

Then open:

```text
http://localhost:5000
```

---

## FastAPI Model Serving

The trained model is exposed through a REST API.

### Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | API information |
| `GET` | `/health` | Service and model status |
| `POST` | `/predict` | Generate prediction |
| `POST` | `/retrain` | Retrain and reload model |
| `GET` | `/ui` | Browser interface |
| `GET` | `/docs` | Swagger UI |
| `GET` | `/redoc` | ReDoc |

FastAPI automatically provides OpenAPI documentation for the application.

---

## Input Validation

Prediction requests are validated using **Pydantic**.

Example validation error:

```json
{
  "errors": [
    {
      "field": "ph",
      "message": "Input should be less than or equal to 14"
    }
  ]
}
```

Validation occurs at the API boundary so invalid data can be rejected before
reaching the model.

---

## Missing Model Handling

The API checks whether a serialized model is available.

If no model has been loaded:

```text
POST /predict
```

returns:

```text
HTTP 503 Service Unavailable
```

Example:

```json
{
  "detail": "No model is loaded. Call POST /retrain first."
}
```

This prevents the service from appearing operational when inference is not
actually available.

---

## Prediction Example

Example request:

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "ph": 7.1,
    "Hardness": 204.8,
    "Solids": 20791.3,
    "Chloramines": 7.3,
    "Sulfate": 368.5,
    "Conductivity": 564.3,
    "Organic_carbon": 10.3,
    "Trihalomethanes": 86.9,
    "Turbidity": 2.9
  }'
```

Example response structure:

```json
{
  "prediction": 0,
  "label": "not potable",
  "confidence": 0.82
}
```

The exact confidence depends on the trained model and the submitted sample.

---

## Model Retraining

The `/retrain` endpoint executes the training lifecycle again.

```text
Request
   ↓
Load Dataset
   ↓
Preprocess
   ↓
Train Random Forest
   ↓
Evaluate
   ↓
Create MLflow Run
   ↓
Log Parameters / Metrics
   ↓
Log Metric to Elasticsearch
   ↓
Serialize Model
   ↓
Reload Model in FastAPI
```

This demonstrates how model training and model serving can be connected through
an application interface.

---

## Docker

The application image uses:

```text
python:3.12-slim
```

The container runs as a non-root user and includes a health check against:

```text
http://localhost:8000/health
```

Build and start:

```bash
docker compose up --build
```

Run in detached mode:

```bash
docker compose up --build -d
```

View running services:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs -f
```

Stop:

```bash
docker compose down
```

---

## Docker Compose

The stack contains:

| Service | Port | Purpose |
|---|---:|---|
| FastAPI | 8000 | Model serving |
| Elasticsearch | 9200 | Metric storage |
| Kibana | 5601 | Metric visualization |
| Filebeat | Internal | Container-log forwarding |

MLflow uses a local SQLite backend and is not currently a separate Docker Compose service.

---

## Monitoring and Logging

After model training, evaluation metrics can be sent to Elasticsearch.

Example:

```json
{
  "run_id": "mlflow-run-id",
  "metric": "test_accuracy",
  "value": 0.6676829268292683,
  "timestamp": "UTC ISO-8601 timestamp",
  "source": "water-quality-mlops-pipeline"
}
```

The Elasticsearch index is:

```text
mlops-metrics
```

If Elasticsearch is unavailable, training continues and a warning is logged.

Monitoring therefore remains a secondary operational concern and does not stop
the core model-training pipeline.

### Kibana

Kibana can be used to inspect metrics stored in Elasticsearch.

A data view can be created using:

```text
mlops-metrics*
```

Useful fields include:

- `run_id`
- `metric`
- `value`
- `timestamp`
- `source`

---

## Testing

Tests are implemented with **Pytest** and FastAPI's `TestClient`.

Current checks include:

- `/health` returns successfully;
- service health state is valid;
- `/predict` returns HTTP 503 if no model is loaded;
- dataset split remains internally consistent;
- target is removed from the feature matrix;
- no missing values remain after preprocessing.

Run:

```bash
PYTHONPATH=src pytest -q
```

Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
pytest -q
```

---

## Continuous Integration

The GitHub Actions workflow is located at:

```text
.github/workflows/mlops-ci.yml
```

It runs checks on pushes and pull requests.

The pipeline executes:

```text
Repository Checkout
        ↓
Python Setup
        ↓
Dependency Installation
        ↓
Black Formatting Check
        ↓
Flake8 Linting
        ↓
Bandit Security Scan
        ↓
Pytest
```

The project therefore checks:

- formatting;
- code quality;
- basic security issues;
- automated tests.

---

## Code Quality

Run formatting:

```bash
black src tests
```

Check formatting:

```bash
black --check src tests
```

Lint:

```bash
flake8 src tests --max-line-length=100
```

Security scan:

```bash
bandit -r src
```

Run tests:

```bash
pytest -q
```

---

## Screenshots

### Swagger Prediction Endpoint

<p align="center">
  <img
    src="assets/screenshots/swagger-predict.png"
    alt="Swagger prediction endpoint"
    width="90%"
  >
</p>

---

### Swagger Retraining Endpoint

<p align="center">
  <img
    src="assets/screenshots/swagger-retrain.png"
    alt="Swagger retraining endpoint"
    width="90%"
  >
</p>

---

### Docker Image

<p align="center">
  <img
    src="assets/screenshots/dockerhub-image.png"
    alt="Docker image"
    width="90%"
  >
</p>

---

## Repository Structure

```text
water-quality-prediction-mlops/
│
├── .github/
│   └── workflows/
│       └── mlops-ci.yml
│
├── assets/
│   ├── banner.png
│   └── screenshots/
│
├── data/
│   └── water_potability.csv
│
├── docs/
│   └── architecture.png
│
├── src/
│   └── water_quality/
│       ├── __init__.py
│       ├── api.py
│       ├── cli.py
│       ├── config.py
│       ├── monitoring.py
│       └── pipeline.py
│
├── tests/
│   ├── test_api.py
│   └── test_pipeline.py
│
├── web/
│   └── index.html
│
├── Dockerfile
├── docker-compose.yml
├── filebeat.yml
├── Makefile
├── requirements.txt
└── README.md
```

---

## Known Limitations

The main limitations are intentionally kept visible.

- The Random Forest significantly overfits.
- Recall for potable water is low.
- Hyperparameter optimization is not automated.
- Automated model drift detection is not implemented.
- Successful prediction with a loaded model is not yet fully covered by the current test suite.
- MLflow is not included as a separate Docker Compose service.
- Authentication and authorization are not implemented.
- Rate limiting is not implemented.
- Kibana configuration requires manual setup.
- The monitoring stack is limited compared with a production observability platform.
- The model must not be used for real-world drinking-water safety decisions.

---

## What I Learned

This project reinforced an important distinction:

```text
Building a model
        ≠
Building an ML system
```

A machine-learning system also requires:

- reproducible preprocessing;
- model evaluation;
- experiment tracking;
- artifact management;
- serving;
- validation;
- error handling;
- testing;
- CI;
- containerization;
- monitoring.

The project also made one modelling limitation especially clear:

> **A technically honest evaluation is more useful than presenting a weak model as a strong one.**

The model overfits, and this limitation is intentionally documented rather than
hidden behind a single aggregate metric.

---

## Installation

### Clone

```bash
git clone https://github.com/sarah-falehh/water-quality-prediction-mlops.git
cd water-quality-prediction-mlops
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Windows

```powershell
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Train the Model

### Windows

```powershell
$env:PYTHONPATH="src"
python -m water_quality.cli
```

### Linux / macOS

```bash
PYTHONPATH=src python -m water_quality.cli
```

The default serialized model is stored under:

```text
artifacts/rf_model.joblib
```

---

## Run the API

### Windows

```powershell
$env:PYTHONPATH="src"
uvicorn water_quality.api:app --reload --port 8000
```

### Linux / macOS

```bash
PYTHONPATH=src uvicorn water_quality.api:app --reload --port 8000
```

Then open:

```text
http://localhost:8000/docs
```

---

## Project Scope

This repository is intended for:

- ML engineering practice;
- MLOps experimentation;
- API development;
- Docker experimentation;
- CI/CD learning;
- model-monitoring exploration;
- portfolio demonstration.

It is **not** a medical, environmental-certification or public-safety system.

---

## License

This project is distributed under the MIT License.

See [`LICENSE`](LICENSE).

---

## Author

### Sarah Faleh

Final-year Data Science & AI Engineering student.

Areas of interest:

- Applied AI
- NLP
- RAG
- AI Agents
- Machine Learning
- MLOps
- Backend Engineering

[LinkedIn](https://linkedin.com/in/sarah-faleh) ·
[GitHub](https://github.com/sarah-falehh)
