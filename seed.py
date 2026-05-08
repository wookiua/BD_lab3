import pandas as pd
from sqlalchemy import create_engine
from models.database import Base 


engine = create_engine('postgresql+psycopg2://postgres:27182818@localhost/DB_lab3')


df = pd.read_csv('data/GlobalWeatherRepository.csv')


columns_to_keep = [
    'country', 'wind_degree', 'wind_kph', 'wind_direction', 
    'last_updated', 'sunrise', 'sunset', 'moonrise', 
    'moonset', 'moon_phase', 'moon_illumination'
]

df_filtered = df[columns_to_keep].copy()

df_filtered['last_updated'] = pd.to_datetime(df_filtered['last_updated']).dt.date

print("Uploading data...")
df_filtered.to_sql('weather', engine, if_exists='append', index=False)

print(f"Done {len(df_filtered)} rows into base!")