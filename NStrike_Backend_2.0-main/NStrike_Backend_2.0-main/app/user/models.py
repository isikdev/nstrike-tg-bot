# app/user/models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.database.db_init import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=False)
    balance = Column(Integer, default=0)
    usdt_balance = Column(Float, default=0.0)
    ammo = Column(Integer, default=30)

    bets = relationship("Bet", back_populates="user")
