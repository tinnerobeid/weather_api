import requests
import os
from dotenv import load_dotenv
from app.models.weather import WeatherRequest

load_dotenv()

class WeatherService:
    def __init__(self, db):
        self.db = db
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, city: str, country_code: str = None):
        params = {
            "q": f"{city},{country_code}" if country_code else city,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        
        # Save to DB (optional)
        db_record = WeatherRequest(city=city, country_code=country_code)
        self.db.add(db_record)
        self.db.commit()
        
        return response.json()