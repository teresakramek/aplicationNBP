from schemas import UserCreate
from model import models
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from database.database import get_db

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

db = next(get_db())

def get_password_hash(password):
    return pwd_context.hash(password)

def create_user(user: UserCreate):
    hash = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hash, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(username: str):
    return db.query(models.User).filter(models.User.username == username).first()