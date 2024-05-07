from fastapi import FastAPI
import requests
from datetime import date
from fastapi.middleware.cors import CORSMiddleware
from service.rate import RateService
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# healthcheck
@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.get("/api/rates/{currency}")
def currencies(currency: str, date_from: str | None = None,  date_to: str | None = None):
    if date_from is None:
        date_from = date.today().strftime('%Y-%m-%d')

    if date_to is None:
        date_to = date.today().strftime('%Y-%m-%d')

    rates = RateService().rates(currency, date_from, date_to)

    if rates:
        return rates

    return { "error": f"cannot fetch rates for {currency}" }


@app.get("/api/currencies")
def currencies():
    return {'currencies': ['USD', 'EUR', 'GPB']}
