from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class WeatherRequest(Base):
    __tablename__ = "weather_requests"
    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False)
    country_code = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)