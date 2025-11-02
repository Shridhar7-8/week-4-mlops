
---

# 🌸 MLOps Week 6: Iris Model Training, Deployment & Orchestration

This repository demonstrates a complete **MLOps workflow** for a machine learning project — built as part of an **MLOps assignment**.
It uses the classic **Iris dataset** to train a **Decision Tree Classifier** and implements:
- **Model Training** with DVC for data/model versioning
- **REST API** using FastAPI for model serving
- **Containerization** with Docker
- **Kubernetes Deployment** for orchestration

---

## ✅ Features

This project implements the following **MLOps best practices**:

* **Data & Model Versioning**: Uses **DVC** with **Google Cloud Storage** as remote storage to version datasets and trained models.
* **Model Training Pipeline**: Automated training script with configurable hyperparameters.
* **REST API Service**: FastAPI-based prediction service with health check and prediction endpoints.
* **Containerization**: Multi-stage Docker build that pulls model artifacts from DVC remote.
* **Kubernetes Deployment**: Production-ready K8s configuration with service and deployment manifests.
* **Git Repository**: Standard version control with proper `.gitignore` and `.dvcignore` configurations.

---

## 📂 Project Structure

```
.
├── app/                    # FastAPI application
│   ├── main.py            # API endpoints and model serving logic
│   └── requirements.txt   # API-specific dependencies
├── artifacts/              # Model outputs (tracked by DVC)
│   └── model.joblib.dvc   # DVC pointer to trained model
├── data/                   # Datasets (tracked by DVC)
│   └── iris.csv.dvc       # DVC pointer to Iris dataset
├── k8s/                    # Kubernetes manifests
│   └── deployment.yml     # K8s Deployment and Service configuration
├── Dockerfile              # Multi-stage Docker build for API
├── README.md               # Project documentation
├── requirements.txt        # Training pipeline dependencies
└── train.py                # Model training script
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Docker (for containerization)
- kubectl (for Kubernetes deployment)
- DVC (for data versioning)
- GCP Service Account (for DVC remote access)

---

## 🏋️ Training the Model

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Shridhar7-8/week-4-mlops.git
cd week-4-mlops
```

### 2️⃣ Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3️⃣ Install training dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure DVC remote (if using your own GCS bucket)

```bash
dvc remote modify gcs_remote url gs://<your-bucket-name>
```

Set up authentication:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/service-account-key.json
```

### 5️⃣ Pull data from DVC

```bash
dvc pull
```

### 6️⃣ Train the model

```bash
python train.py --data data/iris.csv --model artifacts/model.joblib --depth 3
```

### 7️⃣ Version the new model (if retrained)

```bash
dvc add artifacts/model.joblib
git add artifacts/model.joblib.dvc
git commit -m "Update trained model"
dvc push
```

---

## 🌐 Running the API Locally

### 1️⃣ Install API dependencies

```bash
cd app
pip install -r requirements.txt
```

### 2️⃣ Ensure model is available

Make sure `artifacts/model.joblib` exists (pull from DVC if needed).

### 3️⃣ Run the FastAPI server

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

### 4️⃣ Test the API

**Health Check:**
```bash
curl http://localhost:8080/health
```

**Prediction:**
```bash
curl -X POST http://localhost:8080/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [[5.1, 3.5, 1.4, 0.2]]}'
```

**Interactive API Documentation:**
Visit `http://localhost:8080/docs` for Swagger UI.

---

## 🐳 Docker Deployment

### Build the Docker image

The Dockerfile uses a multi-stage build that pulls the model from DVC during build time:

```bash
docker build --secret id=gcp-sa-key,src=/path/to/service-account-key.json \
  -t iris-api:latest .
```

### Run the container

```bash
docker run -p 8080:8080 iris-api:latest
```

Access the API at `http://localhost:8080`

---

## ☸️ Kubernetes Deployment

### 1️⃣ Build and push Docker image to registry

```bash
docker tag iris-api:latest <your-registry>/iris-api:latest
docker push <your-registry>/iris-api:latest
```

### 2️⃣ Update the Kubernetes manifest

Edit `k8s/deployment.yml` and replace `IMAGE_PLACEHOLDER` with your image:

```yaml
image: <your-registry>/iris-api:latest
```

### 3️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k8s/deployment.yml
```

### 4️⃣ Check deployment status

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### 5️⃣ Access the service

If using LoadBalancer type:
```bash
kubectl get service iris-api-service
# Use the EXTERNAL-IP to access the API
```

For local testing with port-forward:
```bash
kubectl port-forward service/iris-api-service 8080:80
```

---

## 📊 API Endpoints

### `GET /health`
Health check endpoint to verify API and model status.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### `POST /predict`
Predict Iris species from sepal/petal measurements.

**Request Body:**
```json
{
  "features": [[5.1, 3.5, 1.4, 0.2]]
}
```

**Response:**
```json
{
  "prediction": 0,
  "species_name": "setosa",
  "input_features": [5.1, 3.5, 1.4, 0.2]
}
```

---

## 🛠️ Technologies Used

- **Python 3.9**: Core programming language
- **scikit-learn**: Machine learning library for model training
- **FastAPI**: Modern web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI
- **DVC**: Data Version Control for ML artifacts
- **Docker**: Containerization platform
- **Kubernetes**: Container orchestration
- **Google Cloud Storage**: DVC remote storage backend

---

## 📝 Model Details

- **Algorithm**: Decision Tree Classifier
- **Dataset**: Iris dataset (150 samples, 4 features, 3 classes)
- **Features**: sepal_length, sepal_width, petal_length, petal_width
- **Target Classes**: setosa (0), versicolor (1), virginica (2)
- **Train/Test Split**: 60/40 with stratification
- **Hyperparameters**: max_depth=3, random_state=42

---

⭐ **This project demonstrates a complete MLOps workflow — from training to deployment with proper versioning, containerization, and orchestration.**

---
