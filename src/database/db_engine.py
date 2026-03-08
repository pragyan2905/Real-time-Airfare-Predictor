from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/flights.db"

engine = create_engine(
    DATABASE_URL,
    echo=False
)