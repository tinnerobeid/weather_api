from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.weather import WeatherService
from app.database import get_db

router = APIRouter(prefix="/api/v1", tags=["weather"])

@router.get("/weather")
def get_weather(city: str, country_code: str = None, db: Session = Depends(get_db)):
    try:
        service = WeatherService(db)
        return service.fetch_weather(city, country_code)
    except requests.exceptions.HTTPError:
        raise HTTPException(status_code=400, detail="City not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))