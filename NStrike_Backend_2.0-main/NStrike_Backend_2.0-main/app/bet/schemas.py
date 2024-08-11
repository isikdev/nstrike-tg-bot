# app/bet/schemas.py
from pydantic import BaseModel
from datetime import datetime

class BetBase(BaseModel):
    user_id: int
    amount: float
    odds: float

class BetCreate(BetBase):
    placed_at: datetime

class BetUpdate(BetBase):
    result: str | None = None

class BetInDBBase(BetBase):
    id: int
    result: str | None = None
    placed_at: datetime

    class Config:
        orm_mode = True

class Bet(BetInDBBase):
    pass
