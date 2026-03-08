from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import mlflow.pyfunc
import mlflow


mlflow.set_tracking_uri("http://127.0.0.1:5000")

app = FastAPI()

model = mlflow.pyfunc.load_model("models:/flight_price_model/latest")

app = FastAPI(title="Flight Price Prediction API")


model = mlflow.pyfunc.load_model("models:/flight_price_model/latest")


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