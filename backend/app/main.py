from fastapi import FastAPI
import requests
import json
from datetime import date
from fastapi.middleware.cors import CORSMiddleware

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
def currencies(currency: str, date_from: str | None = None):
    # get from and to dates - requires
    if date_from is None:
        date_from = date.today().strftime('%Y-%m-%d')
        print(date_from)
    
    response = requests.get(f"https://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_from}?format=json")

    if response.status_code == 200:
        return response.json()

    return {
        "error": f"cannot fetch rates for {currency}",
        "code": response.status_code
        }


@app.get("/api/currencies")
def currencies():
    return {'currencies': ['USD', 'EUR', 'GPB']}
