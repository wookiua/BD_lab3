from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Time, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, sessionmaker
import enum

#DATABASE_URL = "postgresql+psycopg2://postgres:27182818@localhost/DB_lab3"
DATABASE_URL = "mysql+pymysql://root:27182818@127.0.0.1/DB_lab3_mysql"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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
    country = Column(String(255))
    wind_degree = Column(Integer)
    wind_kph = Column(Float)
    wind_direction = Column(Enum(WindDirection))
    last_updated = Column(Date)
    
    celestial_data = relationship("CelestialData", back_populates="weather", uselist=False)


class CelestialData(Base):
    __tablename__ = 'celestial_data'

    id = Column(Integer, primary_key=True)
    weather_id = Column(Integer, ForeignKey('weather.id'))

    sunrise = Column(Time)
    sunset = Column(Time)
    moonrise = Column(Time)
    moonset = Column(Time)
    moon_phase = Column(String(255))
    moon_illumination = Column(Integer)


    should_go_outside = Column(Boolean, nullable=True)

    weather = relationship("Weather", back_populates="celestial_data")