import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingestion.flight_api import AmadeusClient
from src.database.repository import save_flights


def run_pipeline():

    client = AmadeusClient()

    df = client.get_flights(
        origin="DEL",
        destination="LHR",
        departure_date="2026-05-10"
    )

    print("\nFetched Flight Data:\n")
    print(df)

    save_flights(df)

    print("\nPipeline execution completed.\n")


if __name__ == "__main__":
    run_pipeline()