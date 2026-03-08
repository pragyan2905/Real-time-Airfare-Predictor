import os
from dotenv import load_dotenv

load_dotenv()

print("API KEY:", os.getenv("AMADEUS_API_KEY"))
print("API SECRET:", os.getenv("AMADEUS_API_SECRET"))