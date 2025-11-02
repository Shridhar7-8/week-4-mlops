import os
import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conlist
from typing import List

# Define the input data schema using Pydantic
class IrisFeatures(BaseModel):
    # We use conlist (constrained list) to ensure it's a list of 4 floats
    features: List[conlist(float, min_items=4, max_items=4)]

app = FastAPI(
    title="Iris Species Predictor API",
    description="API to predict Iris species from sepal/petal measurements."
)

# --- Model Loading ---
model_path = os.path.join('..', 'artifacts', 'model.joblib')
model = None

@app.on_event("startup")
def load_model():
    """Load the model during application startup."""
    global model
    try:
        model = joblib.load(model_path)
        print(f"Model loaded successfully from {model_path}")
    except FileNotFoundError:
        print(f"Error: Model file not found at {model_path}")
        model = None
    except Exception as e:
        print(f"Error loading model: {e}")
        model = None

# Iris species mapping
species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

# --- Endpoints ---
@app.get('/health', tags=["Health Check"])
def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "model_loaded": model is not None}

@app.post('/predict', tags=["Prediction"])
def predict_species(input_data: IrisFeatures):
    """
    Predicts the Iris species.
    
    Expects a JSON payload with a "features" key:
    {
      "features": [
        [5.1, 3.5, 1.4, 0.2]
      ]
    }
    """
    if model is None:
        raise HTTPException(
            status_code=500, 
            detail="Model not loaded. Check server logs."
        )

    try:
        # Get the first (and only) list of features from the input
        features = input_data.features[0]
        
        # Predict
        prediction = model.predict([features])
        species_name = species_map.get(prediction[0], "unknown")

        return {
            "prediction": int(prediction[0]),
            "species_name": species_name,
            "input_features": features
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
