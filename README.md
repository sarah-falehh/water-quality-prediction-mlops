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
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/MLflow-Experiment_Tracking-0194E2?logo=mlflow&logoColor=white">
  <img src="https://img.shields.io/badge/Elasticsearch-Metrics-005571?logo=elasticsearch&logoColor=white">
  <img src="https://img.shields.io/badge/Kibana-Visualization-E8478B?logo=kibana&logoColor=white">
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

# Overview

This repository demonstrates an **end-to-end MLOps workflow** for a binary
water-potability classification problem.

The project is intentionally presented primarily as an **ML engineering
project**, not as a high-performing predictive model.

It covers:

- data preprocessing;
- missing-value handling;
- train/test splitting;
- Random Forest training;
- model evaluation;
- MLflow experiment tracking;
- model serialization;
- FastAPI serving;
- Pydantic validation;
- model retraining through an API;
- Docker containerization;
- Docker Compose orchestration;
- GitHub Actions CI;
- automated tests;
- Elasticsearch metric logging;
- Kibana visualization;
- Filebeat log forwarding.

> [!IMPORTANT]
> The current Random Forest model shows significant overfitting.
>
> The main value of this repository is therefore the **engineering lifecycle
> around the model**, rather than the predictive performance itself.

---

# Why This Project Matters

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
