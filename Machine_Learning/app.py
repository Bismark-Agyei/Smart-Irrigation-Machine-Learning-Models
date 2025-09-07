from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the trained model once at startup
model = joblib.load("irrigation_model.pkl")  # change to your model file

app = FastAPI()

class InputData(BaseModel):
    temperature: float
    humidity: float
    soil_moisture: float
    crop_type: int

@app.get("/")
def read_root():
    return {"message": "Hello, Bismark! Your FastAPI app is running "}

@app.post("/predict")
def predict(data: InputData):
    # Convert input to numpy array for model prediction
    features = np.array([[data.temperature, data.humidity, data.soil_moisture, data.crop_type]])
    
    prediction = model.predict(features)[0]  # Get single prediction
    
    # Format prediction as JSON for actuator node
    return {"prediction": int(prediction)}


