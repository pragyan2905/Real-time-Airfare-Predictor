import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import lightgbm as lgb
import joblib

DATA_PATH = "data/processed/features.csv"
MODEL_PATH = "models/price_model.pkl"

# connect to MLflow server
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("flight_price_prediction")


def load_data():
    df = pd.read_csv(DATA_PATH)
    return df


def prepare_features(df):

    feature_columns = [
        "stops",
        "days_until_departure",
        "route_avg_price",
        "route_price_std",
        "airline_frequency"
    ]

    X = df[feature_columns]
    y = df["price"]

    return X, y


def train_model(X_train, y_train):

    model = lgb.LGBMRegressor(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=6
    )

    model.fit(X_train, y_train)

    return model


def run_training_pipeline():

    print("Loading dataset...")

    df = load_data()

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    with mlflow.start_run():

        print("Training model...")

        model = train_model(X_train, y_train)

        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)

        print("MAE:", mae)

        # log parameters
        mlflow.log_param("model_type", "LightGBM")
        mlflow.log_param("n_estimators", 200)
        mlflow.log_param("learning_rate", 0.05)
        mlflow.log_param("max_depth", 6)

        # log metric
        mlflow.log_metric("MAE", mae)

        # log model artifact
        mlflow.sklearn.log_model(
            model,
            artifact_path="model",
            registered_model_name="flight_price_model"
)

        # save model locally
        joblib.dump(model, MODEL_PATH)

        print("Model saved to:", MODEL_PATH)