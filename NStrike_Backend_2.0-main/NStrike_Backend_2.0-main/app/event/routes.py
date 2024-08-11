# app/event/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db_init import get_session
from app.event import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Event)
async def create_event(event: schemas.EventCreate, db: AsyncSession = Depends(get_session)):
    return await crud.create_event(db, event)

@router.get("/{event_id}", response_model=schemas.Event)
async def read_event(event_id: int, db: AsyncSession = Depends(get_session)):
    db_event = await crud.get_event(db, event_id)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.put("/{event_id}", response_model=schemas.Event)
async def update_event(event_id: int, event: schemas.EventUpdate, db: AsyncSession = Depends(get_session)):
    db_event = await crud.update_event(db, event_id, event)
    if db_event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event

@router.delete("/{event_id}", response_model=schemas.Event)
async def delete_event(event_id: int, db: AsyncSession = Depends(get_session)):
    success = await crud.delete_event(db, event_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted"}

@router.get("/", response_model=list[schemas.Event])
async def read_events(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    events = await crud.get_events(db, skip=skip, limit=limit)
    return events
