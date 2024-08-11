# app/user/schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str | None = None
    username: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    balance: int | None = None
    usdt_balance: float | None = None
    ammo: int | None = None

class UserInDBBase(UserBase):
    id: int
    balance: int
    usdt_balance: float
    ammo: int

    class Config:
        orm_mode = True

class User(UserInDBBase):
    pass
