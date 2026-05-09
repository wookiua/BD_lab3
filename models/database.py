from sqlalchemy import Column, Integer, String, Float, Date, Time, Enum, Boolean
from sqlalchemy.orm import DeclarativeBase
import enum

class Base(DeclarativeBase):
    pass

class WindDirection(str, enum.Enum):
    N = "N"
    S = "S"
    E = "E"
    W = "W"
    NE = "NE"
    NW = "NW"
    SE = "SE"
    SW = "SW"
    NNE = "NNE"
    NNW = "NNW"
    SSE = "SSE"
    SSW = "SSW"
    ENE = "ENE"
    ESE = "ESE"
    WNW = "WNW"
    WSW = "WSW" 

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
    should_go_outside = Column(Boolean, nullable=True)