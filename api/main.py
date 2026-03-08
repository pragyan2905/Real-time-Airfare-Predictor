from fastapi import FastAPI
import mlflow
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# Connect to MLflow server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Load model from MLflow Model Registry
model = mlflow.pyfunc.load_model("models:/flight_price_model/latest")


# Request schema
class FlightFeatures(BaseModel):
    stops: int
    days_until_departure: int
    route_avg_price: float
    route_price_std: float
    airline_frequency: int


@app.get("/")
def home():
    return {"status": "API is running"}


@app.post("/predict")
def predict(data: FlightFeatures):

    # Convert input to dataframe
    df = pd.DataFrame([data.dict()])

    # Predict
    prediction = model.predict(df)[0]

    return {
        "predicted_price": float(prediction)
    }