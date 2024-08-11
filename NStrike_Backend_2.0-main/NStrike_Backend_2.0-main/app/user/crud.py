# app/user/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.user.models import User
from app.user.schemas import UserCreate, UserUpdate

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    return result.scalars().first()

async def get_user_by_username(db: AsyncSession, username: str):
    result = await db.execute(select(User).filter(User.username == username))
    return result.scalars().first()

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(db: AsyncSession, user_id: int, user: UserUpdate):
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        await db.commit()
        await db.refresh(db_user)
    return db_user

async def delete_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user:
        await db.delete(db_user)
        await db.commit()
        return True
    return False

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()
