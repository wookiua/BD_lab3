from sqlalchemy.orm import Session
from models.database import SessionLocal, Weather, CelestialData
from services.logic import update_recommendations

def get_weather_report(db: Session, country_name: str):
   
    results = db.query(Weather).filter(Weather.country == country_name).limit(10).all()

    
    if not results:
        print(f"No records found for country: {country_name}")
        return

    print(f"\nWeather report for {country_name}:")
    print(f"\nShowing first {len(results)}:")
    print("-" * 50)
    
    for res in results:

        celestial = res.celestial_data
        
        if celestial:
            status = "Worth going out" if celestial.should_go_outside else "Stay home"
            print(f"Date: {res.last_updated} | "
                  f"Moon: {celestial.moon_phase} ({celestial.moon_illumination}%) | "
                  f"Verdict: {status}")
        else:
            print(f"Date: {res.last_updated} | No celestial data available for this record.")

def main():
    db = SessionLocal()
    try:

        print("Running data analysis...")
        update_recommendations(db)
        

        while True:
            country = input("\nEnter country name (or 'exit' to quit): ").strip()
            if country.lower() == 'exit':
                break
            
            if country:
                get_weather_report(db, country)
            else:
                print("Please enter a valid country name.")
                
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()