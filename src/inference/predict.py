import mlflow
import pandas as pd

mlflow.set_tracking_uri("http://127.0.0.1:5000")

model = mlflow.pyfunc.load_model("models:/flight_price_model/latest")


def predict_price(features: dict):

    df = pd.DataFrame([features])

    prediction = model.predict(df)[0]

    return float(prediction)