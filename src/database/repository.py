import pandas as pd
from sqlalchemy.orm import sessionmaker
from src.database.db_engine import engine
from src.database.models import FlightPrice, Base

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def save_flights(df: pd.DataFrame):

    session = Session()

    for _, row in df.iterrows():

        flight = FlightPrice(
            origin=row["origin"],
            destination=row["destination"],
            departure_date=row["departure_date"],
            price=row["price"],
            airline=row["airline"],
            stops=row["stops"]
        )

        session.add(flight)

    session.commit()
    session.close()

    print("Flights saved to database")