import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingestion.flight_api import AmadeusClient

client = AmadeusClient()

df = client.get_flights(
    origin="DEL",
    destination="LHR",
    departure_date="2026-05-10"
)

print(df)