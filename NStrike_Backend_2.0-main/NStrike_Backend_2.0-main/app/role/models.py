# app/role/models.py
from sqlalchemy import Column, Integer, String
from app.database.db_init import Base

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
