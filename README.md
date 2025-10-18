

---

# 🌸 MLOps Week 4 Assignment: CI/CD Pipeline for Iris Model

This repository demonstrates a **Continuous Integration (CI)** pipeline for a machine learning project — built as part of an **MLOps assignment**.
It uses the classic **Iris dataset** to train a **Decision Tree Classifier** and implements a full CI workflow using **GitHub Actions**, **DVC**, and **CML**.

---

## ✅ Objectives Covered

This project successfully implements the following **MLOps best practices**:

* **Git Repository Setup**: Established a standard branching strategy with `main` and `dev` branches.
* **Automated Testing**: Created data validation and model evaluation unit tests using `pytest`.
* **Continuous Integration (CI)**: Configured a CI pipeline using **GitHub Actions** that triggers on pushes and pull requests.
* **Data & Model Versioning Integration**: The CI pipeline fetches versioned datasets and models from a **DVC remote (Google Cloud Storage)** before running tests.
* **Automated Reporting**: On every pull request, a **sanity test report** is automatically generated and posted as a comment using **CML (Continuous Machine Learning)**.

---

## 🧩 Development Workflow Overview

The development follows a **standard Git flow**, enhanced with MLOps automation:

1. **Branching** – Create a new feature branch from `dev`.
2. **Development** – Make code changes (e.g., model improvements, new tests).
3. **Push** – Push the feature branch to GitHub.
4. **Pull Request** – Open a PR to merge into `dev` or `main`.
5. **CI Automation** – The GitHub Actions workflow:

   * Sets up a clean environment
   * Installs dependencies
   * Authenticates with the DVC remote
   * Pulls versioned data and model
   * Runs `pytest` for validation and evaluation
   * Posts a **CML report** with test results in the PR
6. **Review & Merge** – Merge after successful checks and approval.

---

## 📂 Project Structure

```
.
├── .dvc/                   # DVC configuration files
├── .github/workflows/      # GitHub Actions CI/CD workflow definitions
│   └── ci.yml
├── artifacts/              # Model outputs (tracked by DVC)
│   └── model.joblib.dvc
├── data/                   # Datasets (tracked by DVC)
│   └── iris.csv.dvc
├── .dvcignore              # Files for DVC to ignore
├── .gitignore              # Files for Git to ignore
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
├── test_model_validation.py # Pytest unit tests
└── train.py                # Model training script
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Shridhar7-8/week-4-mlops.git
cd week-4-mlops
```

### 2️⃣ Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # (For Windows: venv\Scripts\activate)
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure DVC remote (optional)

You’ll need your own **GCS bucket** and **service account credentials**.
If you’re using your own DVC remote:

```bash
dvc remote modify gcs_remote gcs_bucket_name <your-bucket-name>
```

### 5️⃣ Pull data and model from DVC

```bash
dvc pull
```

### 6️⃣ Run tests

```bash
pytest --verbose
```

---

⭐ **This project demonstrates a simple yet complete CI/CD pipeline for ML workflows — integrating data versioning, testing, and reporting into a reproducible process.**

---



