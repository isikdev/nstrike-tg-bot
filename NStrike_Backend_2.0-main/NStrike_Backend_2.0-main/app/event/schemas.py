# app/event/schemas.py
from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    name: str
    start_time: datetime
    end_time: datetime
    description: str | None = None

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class EventInDBBase(EventBase):
    id: int

    class Config:
        orm_mode = True

class Event(EventInDBBase):
    pass

class EventInDB(EventInDBBase):
    pass
