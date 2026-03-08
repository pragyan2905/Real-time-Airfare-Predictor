from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Flight Price Prediction API")

MODEL_PATH = "models/price_model.pkl"

model = joblib.load(MODEL_PATH)


class FlightFeatures(BaseModel):
    stops: int
    days_until_departure: int
    route_avg_price: float
    route_price_std: float
    airline_frequency: int


@app.get("/")
def root():
    return {"status": "API is running"}


@app.get("/health")
def health_check():
    return {"model_loaded": True}


@app.post("/predict")
def predict(features: FlightFeatures):

    df = pd.DataFrame(
        [[
            features.stops,
            features.days_until_departure,
            features.route_avg_price,
            features.route_price_std,
            features.airline_frequency
        ]],
        columns=[
            "stops",
            "days_until_departure",
            "route_avg_price",
            "route_price_std",
            "airline_frequency"
        ]
    )

    prediction = model.predict(df)[0]

    return {
        "input": features,
        "predicted_price": float(prediction)
    }