# app/transaction/schemas.py
from pydantic import BaseModel
from datetime import datetime

class TransactionBase(BaseModel):
    user_id: int
    amount: float
    timestamp: datetime

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionInDBBase(TransactionBase):
    id: int

    class Config:
        orm_mode = True

class Transaction(TransactionInDBBase):
    pass

class TransactionInDB(TransactionInDBBase):
    pass
