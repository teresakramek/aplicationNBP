from fastapi import FastAPI
import requests
import json
from datetime import datetime, date

app = FastAPI()

# healthcheck
@app.get("/")
def hello_world():
    return {"message": "OK"}


@app.get("/api/exchange-rate/{currency}")
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
