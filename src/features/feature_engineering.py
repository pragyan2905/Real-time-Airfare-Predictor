import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/flights.db"
engine = create_engine(DATABASE_URL)


def load_flight_data():
    query = "SELECT * FROM flight_prices"
    df = pd.read_sql(query, engine)
    return df


def create_features(df):

    df["departure_date"] = pd.to_datetime(df["departure_date"])
    today = pd.Timestamp.today()

    df["days_until_departure"] = (df["departure_date"] - today).dt.days

    df["route_avg_price"] = df.groupby(
        ["origin", "destination"]
    )["price"].transform("mean")

    df["route_price_std"] = df.groupby(
        ["origin", "destination"]
    )["price"].transform("std")

    df["airline_frequency"] = df.groupby(
        ["origin", "destination", "airline"]
    )["airline"].transform("count")

    return df


def build_feature_dataset():

    df = load_flight_data()

    df = create_features(df)

    # save processed dataset
    df.to_csv("data/processed/features.csv", index=False)

    return df