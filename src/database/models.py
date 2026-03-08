from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()


class FlightPrice(Base):

    __tablename__ = "flight_prices"

    id = Column(Integer, primary_key=True)

    origin = Column(String)
    destination = Column(String)

    departure_date = Column(String)

    price = Column(Float)

    airline = Column(String)

    stops = Column(Integer)