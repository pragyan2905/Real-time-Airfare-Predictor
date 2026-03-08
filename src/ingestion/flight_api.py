import os
import requests
import pandas as pd
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

API_KEY = os.getenv("AMADEUS_API_KEY")
API_SECRET = os.getenv("AMADEUS_API_SECRET")

TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"


class AmadeusClient:

    def __init__(self):
        self.token = self.authenticate()

    def authenticate(self):

        payload = {
            "grant_type": "client_credentials",
            "client_id": API_KEY,
            "client_secret": API_SECRET
        }

        response = requests.post(TOKEN_URL, data=payload)

        if response.status_code != 200:
            raise Exception(response.text)

        token = response.json()["access_token"]
        logger.info("Authentication successful")

        return token


    def get_flights(self, origin, destination, departure_date):

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        params = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date,
            "adults": 1,
            "max": 10
        }

        response = requests.get(FLIGHT_URL, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(response.text)

        flights = []

        data = response.json()["data"]

        for offer in data:

            price = float(offer["price"]["total"])
            airline = offer["validatingAirlineCodes"][0]
            stops = len(offer["itineraries"][0]["segments"]) - 1

            flights.append({
                "origin": origin,
                "destination": destination,
                "departure_date": departure_date,
                "price": price,
                "airline": airline,
                "stops": stops
            })

        df = pd.DataFrame(flights)

        return df