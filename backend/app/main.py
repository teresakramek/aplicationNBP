from typing import Annotated, Union

from fastapi import FastAPI, HTTPException, Depends, status
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
from service.rate import RateService
from database.database import engine, Base
from model.models import Rate
from database.database import get_db
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from security import authenticate_user, fake_users_db, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_user, get_current_active_user
from schemas import Token, User


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

@app.post("/api/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")

# healthcheck
@app.get("/")
def health_check():
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

    if rates:
        return list(map(lambda rate: rate.read(), rates))
    
    return []



@app.get("/api/currencies")
async def currencies(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    """@TODO move to table of synchornized values"""
    return {'currencies': ['USD', 'EUR', 'GPB']}


@app.get("/api/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user

