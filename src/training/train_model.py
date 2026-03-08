import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import lightgbm as lgb
import joblib


DATA_PATH = "data/processed/features.csv"
MODEL_PATH = "models/price_model.pkl"


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


def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    print("\nModel Evaluation")
    print("----------------")
    print("MAE:", mae)

    return mae


def save_model(model):

    joblib.dump(model, MODEL_PATH)

    print("\nModel saved to:", MODEL_PATH)


def run_training_pipeline():

    print("\nLoading feature dataset...")

    df = load_data()

    X, y = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("\nTraining model...")

    model = train_model(X_train, y_train)

    evaluate_model(model, X_test, y_test)

    save_model(model)


if __name__ == "__main__":

    run_training_pipeline()