from fastapi import FastAPI
from datetime import date, datetime
from fastapi.middleware.cors import CORSMiddleware
from service.rate import RateService
from database.database import engine, Base
from model.models import Rate
from database.database import get_db

Base.metadata.create_all(bind=engine)

db = next(get_db())

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
        date_from = datetime.today().strftime("%Y-%m-%d")

    if date_to is None:
        date_to = datetime.today().strftime("%Y-%m-%d")

    date_from = datetime.strptime(date_from, "%Y-%m-%d")
    date_to = datetime.strptime(date_to, "%Y-%m-%d")

    date_diff = date_to - date_from
    
    if date_diff.days <= 93:
        rates = RateService().rates(currency, date_from, date_to)

        if rates:
            return rates
        
    rates = db.query(Rate).filter(Rate.currency == currency, Rate.rate_date >= date_from, Rate.rate_date <= date_to).all()



    return list(map(lambda rate: rate.read(), rates))



@app.get("/api/currencies")
def currencies():
    """@TODO move to table of synchornized values"""
    return {'currencies': ['USD', 'EUR', 'GPB']}

