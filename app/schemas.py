from pydantic import BaseModel
from typing import Optional

class WeatherRequestSchema(BaseModel):
    city: str
    country_code: Optional[str] = None

class WeatherResponseSchema(BaseModel):
    temperature: float
    description: str
    city: str
    country_code: Optional[str] = None