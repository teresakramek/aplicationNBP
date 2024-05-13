from pydantic import BaseModel
from typing import Union

class User(BaseModel):
    email: Union[str, None] = None


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Union[str, None] = None


class Rate(BaseModel):
    rate: float
    currency: str
