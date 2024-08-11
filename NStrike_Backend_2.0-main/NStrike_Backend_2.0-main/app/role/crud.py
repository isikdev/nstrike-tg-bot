# app/role/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.role.models import Role
from app.role.schemas import RoleCreate, RoleUpdate

async def get_role(db: AsyncSession, role_id: int):
    result = await db.execute(select(Role).filter(Role.id == role_id))
    return result.scalars().first()

async def create_role(db: AsyncSession, role: RoleCreate):
    db_role = Role(**role.dict())
    db.add(db_role)
    await db.commit()
    await db.refresh(db_role)
    return db_role

async def update_role(db: AsyncSession, role_id: int, role: RoleUpdate):
    db_role = await get_role(db, role_id)
    if db_role:
        for key, value in role.dict().items():
            setattr(db_role, key, value)
        await db.commit()
        await db.refresh(db_role)
        return db_role
    return None

async def delete_role(db: AsyncSession, role_id: int):
    db_role = await get_role(db, role_id)
    if db_role:
        await db.delete(db_role)
        await db.commit()
        return True
    return False

async def get_roles(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(select(Role).offset(skip).limit(limit))
    return result.scalars().all()
