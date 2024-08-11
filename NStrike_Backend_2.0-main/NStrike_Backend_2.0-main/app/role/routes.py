# app/role/routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.db_init import get_session
from app.role import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.Role)
async def create_role(role: schemas.RoleCreate, db: AsyncSession = Depends(get_session)):
    return await crud.create_role(db, role)

@router.get("/{role_id}", response_model=schemas.Role)
async def read_role(role_id: int, db: AsyncSession = Depends(get_session)):
    db_role = await crud.get_role(db, role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.put("/{role_id}", response_model=schemas.Role)
async def update_role(role_id: int, role: schemas.RoleUpdate, db: AsyncSession = Depends(get_session)):
    db_role = await crud.update_role(db, role_id, role)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.delete("/{role_id}", response_model=schemas.Role)
async def delete_role(role_id: int, db: AsyncSession = Depends(get_session)):
    success = await crud.delete_role(db, role_id)
    if not success:
        raise HTTPException(status_code=404, detail="Role not found")
    return {"message": "Role deleted"}

@router.get("/", response_model=list[schemas.Role])
async def read_roles(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    roles = await crud.get_roles(db, skip=skip, limit=limit)
    return roles
