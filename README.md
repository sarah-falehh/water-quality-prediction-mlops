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
  Production-oriented machine learning pipeline for water potability prediction,
  covering training, experiment tracking, API serving, containerization,
  continuous integration, logging, and monitoring.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white" alt="Python 3.12">
  <img src="https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/MLflow-Experiment_Tracking-0194E2?logo=mlflow&logoColor=white" alt="MLflow">
  <img src="https://img.shields.io/badge/Elasticsearch-Metric_Logging-005571?logo=elasticsearch&logoColor=white" alt="Elasticsearch">
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

This repository demonstrates an end-to-end **Machine Learning Operations
(MLOps)** workflow for predicting whether a water sample is potable from nine
physicochemical measurements.

The project goes beyond model training and covers the main lifecycle stages of
a production-oriented machine learning application:

- Dataset loading and preprocessing
- Missing-value handling
- Stratified train/test splitting
- Random Forest model training and evaluation
- MLflow experiment tracking and model artifact logging
- FastAPI model serving
- Swagger/OpenAPI documentation
- Model retraining through an API endpoint
- Docker containerization
- Docker Compose service orchestration
- Continuous integration with GitHub Actions
- Test-accuracy metric logging to Elasticsearch
- Kibana visualization support
- Automated API and pipeline tests

The project uses a modular `src` layout so that configuration, training,
inference, monitoring, and command-line functionality remain separated and
maintainable.

---

## Key Features

- Reproducible machine learning training pipeline
- Binary classification of potable and non-potable water
- Median imputation for missing values
- Stratified train/test split
- Class-balanced Random Forest classifier
- FastAPI inference service
- Interactive Swagger and ReDoc documentation
- Prediction confidence returned through `predict_proba`
- Dedicated model-retraining endpoint
- MLflow parameter, metric, and model artifact tracking
- Dockerized backend application
- Docker Compose stack with Elasticsearch, Kibana, and Filebeat
- GitHub Actions CI pipeline
- Black formatting checks
- Flake8 linting
- Bandit security scanning
- Pytest-based automated testing
- Custom browser-based user interface
- Modular Python package under `src/water_quality`

---

## Architecture

The following diagram presents the main components and data flow of the
application.

<p align="center">
  <img
    src="docs/architecture.png"
    alt="Water Quality MLOps architecture"
    width="95%"
  >
</p>

### High-level workflow

```text
Water Potability Dataset
           │
           ▼
CSV Loading
           │
           ▼
Replace Zero pH Values with Missing Values
           │
           ▼
Median Imputation
           │
           ▼
Feature / Target Separation
           │
           ▼
Stratified Train/Test Split
           │
           ▼
Random Forest Training
           │
           ├──────────────► MLflow
           │                  ├── Parameters
           │                  ├── Train Accuracy
           │                  ├── Test Accuracy
           │                  └── Model Artifact
           │
           └──────────────► Elasticsearch
                              └── Test Accuracy Metric
           │
           ▼
Model Evaluation
           │
           ▼
Joblib Model Serialization
           │
           ▼
FastAPI REST Service
           │
           ├── GET  /
           ├── GET  /health
           ├── POST /predict
           ├── POST /retrain
           ├── GET  /ui
           ├── GET  /docs
           └── GET  /redoc
           │
           ▼
Docker Deployment
           │
           ▼
Elasticsearch + Kibana + Filebeat
```

---

## Technology Stack

| Category | Technologies |
|---|---|
| Programming language | Python 3.12 |
| Data processing | Pandas, NumPy |
| Machine learning | Scikit-learn, Random Forest |
| Missing-value handling | Scikit-learn `SimpleImputer` |
| Model evaluation | Accuracy, precision, recall, F1-score, classification report |
| Model serialization | Joblib |
| API development | FastAPI, Uvicorn |
| API validation | Pydantic |
| API documentation | Swagger UI, OpenAPI, ReDoc |
| Experiment tracking | MLflow |
| Containers | Docker, Docker Compose |
| Metric logging | Elasticsearch |
| Visualization | Kibana |
| Container log forwarding | Filebeat |
| Continuous integration | GitHub Actions |
| Testing | Pytest, FastAPI TestClient |
| Code quality | Black, Flake8, Bandit |
| Version control | Git, GitHub |

---

## Project Structure

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
│       ├── dockerhub-image.png
│       ├── swagger-predict.png
│       └── swagger-retrain.png
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
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── docker-compose.yml
├── filebeat.yml
└── requirements.txt
```

---

## Dataset

The project uses the **Water Potability** dataset, which contains
physicochemical measurements associated with drinking-water quality.

### Dataset dimensions

| Property | Value |
|---|---:|
| Number of observations | 3,276 |
| Total columns | 10 |
| Number of input features | 9 |
| Target variable | `Potability` |
| Non-potable samples | 1,998 |
| Potable samples | 1,278 |
| Non-potable proportion | 60.99% |
| Potable proportion | 39.01% |

### Input features

| Feature | Description |
|---|---|
| `ph` | Acid–base balance of the water |
| `Hardness` | Concentration of calcium and magnesium salts |
| `Solids` | Total dissolved solids |
| `Chloramines` | Chloramine concentration |
| `Sulfate` | Sulfate concentration |
| `Conductivity` | Electrical conductivity |
| `Organic_carbon` | Organic carbon concentration |
| `Trihalomethanes` | Trihalomethane concentration |
| `Turbidity` | Water clarity measurement |
| `Potability` | Target: `1` for potable and `0` for non-potable |

### Missing values in the raw dataset

| Feature | Missing values |
|---|---:|
| `ph` | 491 |
| `Sulfate` | 781 |
| `Trihalomethanes` | 162 |
| Other columns | 0 |

### Preprocessing

The implemented preprocessing pipeline:

1. Loads the dataset from CSV.
2. Replaces zero values in `ph` with `NaN`.
3. Applies median imputation to every dataset column.
4. Separates the nine input variables from `Potability`.
5. Converts the target variable to integers.
6. Creates an 80/20 stratified train/test split.

> **Disclaimer:** This project is intended for educational and demonstration
> purposes only. Its predictions must not replace certified laboratory
> water-quality testing or professional health and safety assessments.

---

## Model Configuration

The production model uses the following configuration:

| Parameter | Value |
|---|---|
| Estimator | Random Forest Classifier |
| Number of estimators | 300 |
| Maximum depth | None |
| Random state | 42 |
| Class weighting | Balanced |
| Training set | 80% |
| Test set | 20% |
| Split strategy | Stratified |
| Missing-value strategy | Median imputation |
| Model serialization | Joblib |

The retraining endpoint allows users to customize:

| Parameter | Accepted values |
|---|---|
| `n_estimators` | 10 to 2,000 |
| `max_depth` | `null` or 1 to 100 |
| `random_state` | Integer |

---

## Model Performance

The metrics below were reproduced using the exact pipeline implemented in
`src/water_quality/pipeline.py`:

```python
RandomForestClassifier(
    n_estimators=300,
    max_depth=None,
    random_state=42,
    class_weight="balanced",
)
```

The evaluation set contains **656 observations**:

- 400 non-potable samples
- 256 potable samples

### Overall metrics

| Metric | Score |
|---|---:|
| Training accuracy | 1.0000 |
| Test accuracy | 0.6677 |
| Macro precision | 0.6723 |
| Macro recall | 0.5981 |
| Macro F1-score | 0.5842 |
| Weighted precision | 0.6708 |
| Weighted recall | 0.6677 |
| Weighted F1-score | 0.6251 |

### Per-class performance

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Non-potable (`0`) | 0.6655 | 0.9150 | 0.7705 | 400 |
| Potable (`1`) | 0.6792 | 0.2812 | 0.3978 | 256 |

### Confusion matrix

|  | Predicted non-potable | Predicted potable |
|---|---:|---:|
| Actual non-potable | 366 | 34 |
| Actual potable | 184 | 72 |

### Interpretation

The model is strong at identifying **non-potable water**, reaching a recall of
**91.50%** for class `0`.

However, its recall for potable water is lower at **28.12%**, meaning that many
potable samples are classified as non-potable. The perfect training accuracy
combined with a test accuracy of approximately **66.77%** also suggests
overfitting.

This behavior makes the project a useful MLOps demonstration while highlighting
several machine-learning improvements that could be explored:

- Hyperparameter optimization
- Cross-validation
- Probability-threshold tuning
- Alternative classifiers
- Feature selection
- Resampling strategies
- Calibration
- More advanced preprocessing
- Ensemble comparison

---

## MLflow Experiment Tracking

The training function creates or reuses the following MLflow experiment:

```text
WaterPotability
```

The default tracking backend is:

```text
sqlite:///mlflow.db
```

Each training run logs:

### Parameters

- `n_estimators`
- `max_depth`
- `random_state`

### Metrics

- `train_accuracy`
- `test_accuracy`

### Artifacts

- Scikit-learn model
- Input example containing five training rows

The model is logged under:

```text
model
```

### Start the MLflow interface

After training at least one model, run:

```bash
mlflow ui \
  --backend-store-uri sqlite:///mlflow.db \
  --host 0.0.0.0 \
  --port 5000
```

On Windows PowerShell, the command can be written on one line:

```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 5000
```

Open:

```text
http://localhost:5000
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Return the API name and links to the documentation and UI |
| `GET` | `/health` | Return service health and model-loading status |
| `POST` | `/predict` | Predict whether a water sample is potable |
| `POST` | `/retrain` | Retrain, save, and reload the Random Forest model |
| `GET` | `/ui` | Display the custom browser interface |
| `GET` | `/docs` | Display interactive Swagger documentation |
| `GET` | `/redoc` | Display ReDoc documentation |

### API metadata

| Property | Value |
|---|---|
| Title | Water Quality MLOps API |
| Version | 2.0.0 |
| Framework | FastAPI |
| Documentation | Swagger UI and ReDoc |

---

## Input Validation

The prediction endpoint validates each measurement through Pydantic.

| Field | Accepted range |
|---|---:|
| `ph` | 0 to 14 |
| `Hardness` | 0 to 500 |
| `Solids` | 0 to 50,000 |
| `Chloramines` | 0 to 20 |
| `Sulfate` | 0 to 1,000 |
| `Conductivity` | 0 to 2,000 |
| `Organic_carbon` | 0 to 100 |
| `Trihalomethanes` | 0 to 300 |
| `Turbidity` | 0 to 20 |

Validation errors are returned as structured JSON:

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

---

## Installation

### Prerequisites

Install the following tools:

- Python 3.12
- Git
- Docker
- Docker Compose

### Clone the repository

```bash
git clone https://github.com/sarah-falehh/water-quality-prediction-mlops.git
cd water-quality-prediction-mlops
```

### Create a virtual environment

```bash
python -m venv .venv
```

### Activate it on Windows

```powershell
.venv\Scripts\activate
```

### Activate it on Linux or macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

## Train the Model

The API requires a serialized model before `/predict` can be used.

Run the command-line training script:

### Linux or macOS

```bash
PYTHONPATH=src python -m water_quality.cli
```

### Windows PowerShell

```powershell
$env:PYTHONPATH="src"
python -m water_quality.cli
```

The default model is saved to:

```text
artifacts/rf_model.joblib
```

Expected console output:

```text
Model saved to artifacts/rf_model.joblib; test accuracy=0.6677
```

### Customize training

```powershell
$env:PYTHONPATH="src"
python -m water_quality.cli --n-estimators 500 --max-depth 20
```

---

## Run the API Locally

### Linux or macOS

```bash
PYTHONPATH=src uvicorn water_quality.api:app --reload --port 8000
```

### Windows PowerShell

```powershell
$env:PYTHONPATH="src"
uvicorn water_quality.api:app --reload --port 8000
```

Available interfaces:

| Interface | Address |
|---|---|
| API root | `http://localhost:8000` |
| Health endpoint | `http://localhost:8000/health` |
| Custom UI | `http://localhost:8000/ui` |
| Swagger UI | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |

---

## Prediction API Usage

The API must have a trained model loaded. When no serialized model exists, the
prediction endpoint returns HTTP `503`:

```json
{
  "detail": "No model is loaded. Call POST /retrain first."
}
```

### Prediction request

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

### Response structure

```json
{
  "prediction": 0,
  "label": "not potable",
  "confidence": 0.82
}
```

The exact confidence depends on the trained model and submitted measurements.

The output fields are:

| Field | Description |
|---|---|
| `prediction` | Binary model prediction: `0` or `1` |
| `label` | `not potable` or `potable` |
| `confidence` | Probability assigned to the predicted class |

---

## Model Retraining API

The retraining endpoint:

1. Reads the dataset.
2. Repeats preprocessing.
3. Trains a new Random Forest.
4. Creates an MLflow run.
5. Logs parameters and metrics.
6. Logs the model artifact.
7. Sends test accuracy to Elasticsearch when available.
8. Saves the model using Joblib.
9. Reloads the new model into the running FastAPI application.

### Retraining request with default parameters

```bash
curl -X POST "http://localhost:8000/retrain" \
  -H "Content-Type: application/json" \
  -d '{
    "n_estimators": 300,
    "max_depth": null,
    "random_state": 42
  }'
```

### Response

```json
{
  "status": "success",
  "test_accuracy": 0.6676829268292683,
  "parameters_used": {
    "n_estimators": 300,
    "max_depth": null,
    "random_state": 42
  }
}
```

---

## Run with Docker

The Docker image uses:

```text
python:3.12-slim
```

The application runs as a non-root user and includes a health check against:

```text
http://localhost:8000/health
```

### Build and start the complete stack

```bash
docker compose up --build
```

### Run in detached mode

```bash
docker compose up --build -d
```

### View running containers

```bash
docker compose ps
```

### View logs

```bash
docker compose logs -f
```

### Stop the stack

```bash
docker compose down
```

### Remove containers and volumes

```bash
docker compose down -v
```

### Docker Compose services

| Service | Port | Description |
|---|---:|---|
| FastAPI API | 8000 | Prediction, retraining, health check, and UI |
| Elasticsearch | 9200 | Stores model-evaluation metrics |
| Kibana | 5601 | Explores and visualizes Elasticsearch data |
| Filebeat | Internal | Forwards Docker container logs |

> MLflow is configured with a local SQLite backend but is not currently defined
> as a separate Docker Compose service.

---

## Monitoring and Logging

The training pipeline sends the following document to Elasticsearch after a
successful MLflow run:

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
Monitoring failures therefore do not interrupt the model-training pipeline.

### Elasticsearch

Open:

```text
http://localhost:9200
```

Check the metrics index:

```bash
curl "http://localhost:9200/mlops-metrics/_search?pretty"
```

### Kibana

Open:

```text
http://localhost:5601
```

Create a data view using:

```text
mlops-metrics*
```

Useful fields include:

- `run_id`
- `metric`
- `value`
- `timestamp`
- `source`

### Filebeat

Filebeat is configured as part of the Docker Compose stack to read Docker
container logs and forward them to Elasticsearch.

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
    alt="Swagger model retraining endpoint"
    width="90%"
  >
</p>

---

### Docker Image

<p align="center">
  <img
    src="assets/screenshots/dockerhub-image.png"
    alt="Docker Hub image repository"
    width="90%"
  >
</p>

---

## Testing

Run the complete test suite:

### Linux or macOS

```bash
PYTHONPATH=src pytest -q
```

### Windows PowerShell

```powershell
$env:PYTHONPATH="src"
pytest -q
```

Run verbose tests:

```powershell
$env:PYTHONPATH="src"
pytest -v
```

### Current automated checks

The test suite currently verifies:

- `/health` returns a successful response
- The API reports a healthy service state
- `/predict` returns HTTP `503` when no model is loaded
- The dataset split remains internally consistent
- The target is removed from the feature matrix
- No missing values remain after preprocessing

---

## Code Quality

### Format code

```bash
black src tests
```

### Verify formatting

```bash
black --check src tests
```

### Run linting

```bash
flake8 src tests --max-line-length=100
```

### Run security analysis

```bash
bandit -r src
```

### Run all Makefile checks

```bash
make format
make lint
make security
make test
```

---

## Continuous Integration

The workflow is located at:

```text
.github/workflows/mlops-ci.yml
```

It runs on:

- Pushes to `main`
- Pushes to `master`
- Pushes to `dev`
- Pull requests

The CI job performs:

1. Repository checkout
2. Python 3.12 setup
3. Pip dependency caching
4. Dependency installation
5. Black formatting verification
6. Flake8 linting
7. Bandit security scanning
8. Pytest execution

The test command executed in CI is:

```bash
PYTHONPATH=src pytest -q
```

---

## Configuration

The project supports environment-variable overrides.

| Variable | Default value |
|---|---|
| `DATA_PATH` | `data/water_potability.csv` |
| `MODEL_PATH` | `artifacts/rf_model.joblib` |
| `MLFLOW_TRACKING_URI` | `sqlite:///mlflow.db` |
| `ELASTICSEARCH_URL` | `http://localhost:9200` |

Docker Compose overrides:

| Variable | Docker value |
|---|---|
| `DATA_PATH` | `/app/data/water_potability.csv` |
| `MODEL_PATH` | `/app/artifacts/rf_model.joblib` |
| `ELASTICSEARCH_URL` | `http://elasticsearch:9200` |

---

## Security and Data Protection

- API credentials and secrets should be stored in environment variables.
- `.env` files must never be committed.
- MLflow run folders and SQLite databases should remain excluded from Git.
- Serialized models should be stored in controlled artifact storage for
  production use.
- The Docker application runs as a non-root user.
- Production deployment should add authentication and authorization.
- Production deployment should enforce HTTPS.
- Rate limiting should be enabled before exposing the API publicly.
- Uploaded or external data should be validated before model processing.

---

## Known Limitations

- The model shows significant overfitting.
- Recall for potable water is low.
- The current pipeline evaluates one default estimator configuration.
- MLflow is not currently included as a Docker Compose service.
- The API does not currently implement authentication.
- The API does not currently implement rate limiting.
- The Kibana dashboard must be configured manually.
- Automated model drift detection is not implemented.
- Hyperparameter optimization is not automated.
- The current automated tests do not yet cover successful predictions with a
  loaded model.
- This model must not be used for real-world drinking-water safety decisions.

---


## License

This project is distributed under the MIT License.

See the [`LICENSE`](LICENSE) file for details.

---

## Author

### Sarah Faleh

Final-year Software Engineering student specializing in **Data Science and
Artificial Intelligence**.

Areas of interest:

- Machine Learning
- MLOps
- Generative AI
- Large Language Models
- AI automation
- Backend engineering
- Production-oriented AI systems

Connect with me:

- [LinkedIn](https://linkedin.com/in/sarah-faleh)
- [GitHub](https://github.com/sarah-falehh)
