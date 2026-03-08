import sys
import os
import pandas as pd

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingestion.flight_api import AmadeusClient
from src.database.repository import save_flights


def run_pipeline():

    client = AmadeusClient()

    routes = [
        ("DEL", "LHR"),
        ("DEL", "DXB"),
        ("DEL", "SIN"),
        ("DEL", "BOM"),
        ("DEL", "JFK"),
    ]

    dates = [
        "2026-05-10",
        "2026-06-10",
        "2026-07-10"
    ]

    all_data = []

    for origin, destination in routes:
        for departure_date in dates:

            df = client.get_flights(
                origin=origin,
                destination=destination,
                departure_date=departure_date
            )

            all_data.append(df)

    df = pd.concat(all_data, ignore_index=True)

    print("\nCollected Data:\n")
    print(df.head())

    save_flights(df)

    print("\nPipeline execution completed.\n")


if __name__ == "__main__":
    run_pipeline()