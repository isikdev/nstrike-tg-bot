# app/user/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db_init import get_session
from app.user import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_session)):
    db_user = await crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return await crud.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_session)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user: schemas.UserUpdate, db: AsyncSession = Depends(get_session)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.update_user(db=db, user_id=user_id, user=user)

@router.delete("/{user_id}", response_model=schemas.User)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_session)):
    db_user = await crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.delete_user(db=db, user_id=user_id)

@router.get("/", response_model=list[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_session)):
    users = await crud.get_users(db, skip=skip, limit=limit)
    return users
