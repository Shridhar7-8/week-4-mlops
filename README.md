MLOps Week 4 Assignment: CI/CD Pipeline for Iris Model
This repository is a practical demonstration of a Continuous Integration (CI) pipeline for a machine learning project, built as part of an MLOps assignment. The project uses the classic Iris dataset to train a Decision Tree classifier and implements a full CI workflow using GitHub Actions, DVC for data versioning, and CML for reporting.
✅ Objectives Covered
This project successfully implements the following MLOps practices:
Git Repository Setup: Established a standard branching strategy with main and dev branches.
Automated Testing: Created data validation and model evaluation unit tests using pytest.
Continuous Integration (CI): Configured a CI pipeline using GitHub Actions that triggers on pushes and pull requests.
Data & Model Versioning Integration: The CI pipeline is configured to fetch versioned datasets and models directly from a DVC remote (Google Cloud Storage) before running tests.
Automated Reporting: On every pull request, a sanity test report is automatically generated and posted as a comment using CML (Continuous Machine Learning).
workflow
Development Workflow Overview
The development process follows a standard Git flow, enhanced with MLOps automation:
Branching: A new feature branch is created from dev.
Development: Code changes (e.g., model improvements, new tests) are made on the feature branch.
Push: The feature branch is pushed to the remote GitHub repository.
Pull Request: A Pull Request is created to merge the changes into the dev or main branch.
CI Automation: This action triggers the GitHub Actions workflow, which:
Sets up a clean environment.
Installs all dependencies.
Authenticates with the DVC remote storage.
Pulls the exact version of the data and model needed for the tests.
Runs the pytest suite for data validation and model evaluation.
Posts a CML report with the test results back to the pull request.
Review & Merge: If all checks pass and the code is approved, the pull request is merged.
📂 Project Structure
.
├── .dvc/                   # DVC configuration files
├── .github/workflows/      # GitHub Actions CI/CD workflow definitions
│   └── ci.yml
├── artifacts/              # Directory for model outputs (tracked by DVC)
│   └── model.joblib.dvc
├── data/                   # Directory for datasets (tracked by DVC)
│   └── iris.csv.dvc
├── .dvcignore              # Files for DVC to ignore
├── .gitignore              # Files for Git to ignore
├── README.md               # This file
├── requirements.txt        # Project dependencies
├── test_model_validation.py # Pytest unit tests
└── train.py                # Model training script


🚀 How to Run Locally
To run this project on your own machine:
Clone the repository:
git clone [https://github.com/Shridhar7-8/week-4-mlops.git](https://github.com/Shridhar7-8/week-4-mlops.git)
cd week-4-mlops


Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Configure DVC remote:
You will need your own GCS bucket and service account credentials.
# (Optional) If you are using your own DVC remote
dvc remote modify gcs_remote gcs_bucket_name <your-bucket-name>


Pull data and model from DVC:
dvc pull


Run tests:
pytest --verbose



