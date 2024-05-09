from sqlalchemy import Column, Integer, String, Date
from database.database import Base
from sqlalchemy.ext.hybrid import hybrid_property


class Rate(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True)
    currency = Column(String, index=True)
    rate = Column(Integer)
    rate_date = Column(Date, index=True)

    @hybrid_property
    def rate_value(self) -> float:
        return self.rate / 1000
    
    def read(self):
        return {
            "rate": self.rate_value,
            "date": self.rate_date
        }



class Currency(Base):
    """Dodanie zmigrowanych walut, dodanie relacji"""
    __tablename__ = "currency"

    id = Column(Integer, primary_key=True)
    code = Column(String, index=True)
    name = Column(String)