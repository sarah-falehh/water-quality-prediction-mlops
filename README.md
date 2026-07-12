<p align="center">
  <img src="assets/banner.png" alt="Banner">
</p>

<h1 align="center">💧 Water Quality Prediction - End-to-End MLOps Pipeline</h1>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker)
![MLflow](https://img.shields.io/badge/MLflow-0194E2)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions)
![ElasticSearch](https://img.shields.io/badge/Elasticsearch-005571?logo=elasticsearch)
![Kibana](https://img.shields.io/badge/Kibana-E8478B?logo=kibana)

</p>

---

# 📖 Overview

This project demonstrates a complete **Machine Learning Operations (MLOps)** workflow for predicting water potability.

Rather than focusing only on model training, the project covers the entire lifecycle of a production-ready ML system:

- Data preprocessing
- Model training
- Experiment tracking
- REST API deployment
- Containerization
- Continuous Integration
- Monitoring & Logging

---

# 🚀 Features

✅ Machine Learning Pipeline

✅ FastAPI REST API

✅ Interactive Swagger Documentation

✅ Docker & Docker Compose

✅ MLflow Experiment Tracking

✅ GitHub Actions CI

✅ Elasticsearch Logging

✅ Kibana Dashboard

✅ Retraining Endpoint

---

# 🏗 Architecture

<p align="center">

<img src="docs/architecture.png" width="95%">

</p>

---

# 🧠 Machine Learning Pipeline

Dataset

↓

Data Cleaning

↓

Feature Engineering

↓

Train / Test Split

↓

Random Forest Model

↓

Evaluation

↓

Model Serialization

↓

REST API

↓

Docker Deployment

↓

Monitoring

---

# ⚙️ Tech Stack

| Category | Technologies |
|------------|--------------------------------|
| Language | Python |
| ML | Scikit-Learn |
| API | FastAPI |
| Documentation | Swagger / OpenAPI |
| Tracking | MLflow |
| Containers | Docker |
| CI/CD | GitHub Actions |
| Monitoring | Elasticsearch • Kibana |

---

# 📂 Project Structure

```text
.
├── assets
├── data
├── docs
├── src
├── tests
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 📊 API Endpoints

| Endpoint | Description |
|-----------|---------------------------|
| POST /predict | Predict water potability |
| POST /retrain | Retrain the ML model |
| GET /docs | Swagger UI |

---

# 📸 Screenshots

## Swagger - Prediction Endpoint

![](assets/screenshots/swagger-predict.png)

---

## Swagger - Retraining Endpoint

![](assets/screenshots/swagger-retrain.png)

---

## Docker Image

![](assets/screenshots/dockerhub-image.png)

---

# 🐳 Run with Docker

```bash
docker compose up --build
```

---

# 📈 Monitoring

This project integrates:

- Elasticsearch
- Kibana
- Request Logging
- Prediction Logging
- Retraining Logging

---

# 🔬 Experiment Tracking

MLflow is used to:

- Track experiments
- Log parameters
- Log metrics
- Compare runs
- Store trained models

---

# 🎯 Future Improvements

- Kubernetes Deployment

- AWS / Azure Deployment

- Model Registry

- Prometheus & Grafana

- Automated Retraining

- Drift Detection

---

# 👩‍💻 Author

## Sarah Faleh

Final-Year Software Engineering Student

**Specialization:** Data Science & Artificial Intelligence

Interested in:

- Machine Learning
- MLOps
- Generative AI
- Software Engineering

LinkedIn: [linkedin.com/in/sarah-faleh](https://linkedin.com/in/sarah-faleh)
