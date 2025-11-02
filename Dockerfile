# --- Build Stage ---
FROM python:3.9-slim as builder
WORKDIR /build
RUN pip install "dvc[gcs]"
COPY .dvc .dvc
COPY artifacts/model.joblib.dvc artifacts/
COPY .dvcignore .dvcignore
RUN dvc pull artifacts/model.joblib -r gcs_remote --force

# --- Final Stage ---
FROM python:3.9-slim
WORKDIR /app
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
COPY --from=builder /build/artifacts/model.joblib /artifacts/model.joblib
EXPOSE 8080

# === THIS IS THE ONLY LINE THAT CHANGES ===
# Run the app using Uvicorn
# "main:app" means "the 'app' object inside the 'main.py' file"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
