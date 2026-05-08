from sqlalchemy import Column, Integer, String, Float, Date, Time, Enum
from sqlalchemy.orm import DeclarativeBase
import enum

class Base(DeclarativeBase):
    pass

class WindDirection(str, enum.Enum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"
    NW = "NW"
    NE = "NE"
    SW = "SW"
    SE = "SE" 

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    wind_degree = Column(Integer)
    wind_kph = Column(Float)
    wind_direction = Column(Enum(WindDirection))
    last_updated = Column(Date)
    
    sunrise = Column(Time)
    sunset = Column(Time)
    moonrise = Column(Time)
    moonset = Column(Time)
    moon_phase = Column(String)
    moon_illumination = Column(Integer)