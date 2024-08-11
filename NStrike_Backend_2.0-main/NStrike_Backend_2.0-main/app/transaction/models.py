# app/transaction/models.py
from sqlalchemy import Column, Integer, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from app.database.db_init import Base

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    user = relationship('User', back_populates='transactions')
