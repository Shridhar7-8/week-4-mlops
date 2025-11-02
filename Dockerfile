# --- Build Stage ---
# Use a full Python image to install dependencies
FROM python:3.9-slim as builder

WORKDIR /build

# Install git (which DVC needs) and DVC with Google Storage support
RUN apt-get update && apt-get install -y git && \
    pip install "dvc[gs]"

# Initialize a dummy git repository so DVC doesn't complain
RUN git init

# Copy only the DVC files needed to pull
COPY .dvc .dvc
COPY artifacts/model.joblib.dvc artifacts/
COPY .dvcignore .dvcignore

# Mount the secret key file, set it as the credentials, and then pull.
# The 'gcp-sa-key' secret is passed in via the 'docker build' command in the cd.yml workflow.
RUN --mount=type=secret,id=gcp-sa-key,dst=/tmp/gcp_sa_key.json \
    export GOOGLE_APPLICATION_CREDENTIALS=/tmp/gcp_sa_key.json && \
    dvc pull artifacts/model.joblib -r gcs_remote --force

# --- Final Stage ---
# Use a lightweight image for the final container
FROM python:3.9-slim

WORKDIR /app

# Copy API requirements and install them
COPY app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the API application code
COPY app/ .

# Copy the model we pulled in the builder stage
COPY --from=builder /build/artifacts/model.joblib /artifacts/model.joblib

# Expose the port the app will run on
EXPOSE 8080

# Run the app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]


