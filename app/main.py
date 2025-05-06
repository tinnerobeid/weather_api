# FastApi initialization
from fastapi import FastAPI
from app.database import Base, engine
from app.api.weather import router as weather_router  # Fixed import path

Base.metadata.create_all(bind=engine)  # Create tables

app = FastAPI()
app.include_router(weather_router)

@app.get("/")
def root():
    return {"message": "Weather API is running"}