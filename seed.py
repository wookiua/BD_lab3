import pandas as pd
from sqlalchemy import create_engine

#engine = create_engine('postgresql+psycopg2://postgres:27182818@localhost/DB_lab3')
engine = create_engine('mysql+pymysql://root:27182818@127.0.0.1/DB_lab3_mysql')

df = pd.read_csv('data/GlobalWeatherRepository.csv')


df['last_updated'] = pd.to_datetime(df['last_updated']).dt.date

time_columns = ['sunrise', 'sunset', 'moonrise', 'moonset']
for col in time_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce').dt.time

print("Data cleaned. Starting upload...")

weather_cols = ['country', 'wind_degree', 'wind_kph', 'wind_direction', 'last_updated']
df_weather = df[weather_cols].copy()
df_weather.to_sql('weather', engine, if_exists='append', index=False)
print("Table 'weather' populated.")

celestial_cols = ['sunrise', 'sunset', 'moonrise', 'moonset', 'moon_phase', 'moon_illumination']
df_celestial = df[celestial_cols].copy()

df_celestial['weather_id'] = range(1, len(df_celestial) + 1)

df_celestial.to_sql('celestial_data', engine, if_exists='append', index=False)
print("Table 'celestial_data' populated. Migration successful!")
print(f"Connected to: {engine.url}")