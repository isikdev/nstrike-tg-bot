# app/event/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.event.models import Event
from app.event.schemas import EventCreate, EventUpdate

async def get_event(db: AsyncSession, event_id: int):
    result = await db.execute(select(Event).filter(Event.id == event_id))
    return result.scalars().first()

async def create_event(db: AsyncSession, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    await db.commit()
    await db.refresh(db_event)
    return db_event

async def update_event(db: AsyncSession, event_id: int, event: EventUpdate):
    db_event = await get_event(db, event_id)
    if db_event:
        for key, value in event.dict().items():
            setattr(db_event, key, value)
        await db.commit()
        await db.refresh(db_event)
        return db_event
    return None

async def delete_event(db: AsyncSession, event_id: int):
    db_event = await get_event(db, event_id)
    if db_event:
        await db.delete(db_event)
        await db.commit()
        return True
    return False

async def get_events(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Event).offset(skip).limit(limit))
    return result.scalars().all()
