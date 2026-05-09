from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from services.logic import get_moon_data_by_country, update_recommendations

engine = create_engine('postgresql+psycopg2://postgres:27182818@localhost/DB_lab3')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def main():
    db = SessionLocal()
    try:

        print("\nBeginn")
        update_recommendations(db)


        country = input("\nEnter country name: ")
        results = get_moon_data_by_country(db, country)
        
        print(f"\nRecords found for {country}: {len(results)}")
        for r in results[:10]:
            status = "Worth going out (Bright moon)" if r.should_go_outside else "Stay home (Too dark)"
            print(f"Date: {r.last_updated} | Illumination: {r.moon_illumination}% | Verdict: {status}")
            
    finally:
        db.close()

if __name__ == "__main__":
    main()