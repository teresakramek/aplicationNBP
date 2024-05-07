from sqlalchemy import Column, Integer, String, Date

from database import Base

class User(Base):
    __tablename__ = "rates"

    id = Column(Integer, primary_key=True)
    currency = Column(String, index=True)
    rate = Column(Integer)
    rate_date = Column(Date, index=True)