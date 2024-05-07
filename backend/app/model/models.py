from sqlalchemy import Column, Integer, String, Date
from database.database import Base


class Rate(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True)
    currency = Column(String, index=True)
    rate = Column(Integer)
    rate_date = Column(Date, index=True)


class Currency(Base):
    """Dodanie zmigrowanych walut, dodanie relacji"""
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    code = Column(String, index=True)
    name = Column(String)