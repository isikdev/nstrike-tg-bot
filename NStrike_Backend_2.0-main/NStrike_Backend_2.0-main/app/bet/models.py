# app/bet/models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database.db_init import Base

class Bet(Base):
    __tablename__ = 'bets'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    amount = Column(Float, nullable=False)
    odds = Column(Float, nullable=False)
    result = Column(String, nullable=True)
    placed_at = Column(DateTime, nullable=False)

    user = relationship("User", back_populates="bets")
