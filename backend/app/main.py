from typing import Annotated

from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.sql import text
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware
from service.rate import RateService
from database.database import engine, Base
from model.models import Rate
from database.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from security.security import authenticate_user, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, get_current_active_user
from schemas.schemas import Token, User, UserCreate, UserBase
import user.user_manager as user_manager
import os

Base.metadata.create_all(bind=engine)

db = next(get_db())


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4200'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# healthcheck
@app.get("/")
def health_check():
    return {"message": "OK"}


@app.post("/api/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@app.post("/api/register", response_model=UserBase)
async def create_user(user: UserCreate):
    db_user = user_manager.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_manager.create_user(user=user)


@app.get("/api/rates/{currency}")
async def currencies(current_user: Annotated[User, Depends(get_current_active_user)], currency: str, date_from: str | None = None,  date_to: str | None = None):

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
    result = db.execute(text("SELECT DISTINCT currency FROM rates;")).fetchall()
    map_result =  [currency[0] for currency in result]

    return {"currencies": map_result}


@app.get("/api/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user




