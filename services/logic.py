from sqlalchemy.orm import Session
from models.database import Weather

def get_moon_data_by_country(db: Session, country_name: str, min_illumination: int = 50):
    return db.query(Weather).filter(
        Weather.country == country_name,
        Weather.moon_illumination >= min_illumination
    ).all()

def update_recommendations(db: Session):
 
    records = db.query(Weather).all()
    
    for record in records:

        if record.moon_illumination is not None:

            record.should_go_outside = record.moon_illumination > 50
        else:
            record.should_go_outside = False
            
    db.commit()
    print(f"\nCelestial Bodies category. Updated {len(records)} records.")