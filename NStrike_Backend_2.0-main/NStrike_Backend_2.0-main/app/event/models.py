# app/event/models.py
from sqlalchemy import Column, Integer, String, DateTime
from app.database.db_init import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
