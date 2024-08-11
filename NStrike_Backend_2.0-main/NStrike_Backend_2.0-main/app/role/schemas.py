# app/role/schemas.py
from pydantic import BaseModel

class RoleBase(BaseModel):
    name: str
    description: str | None = None

class RoleCreate(RoleBase):
    pass

class RoleUpdate(RoleBase):
    pass

class RoleInDBBase(RoleBase):
    id: int

    class Config:
        orm_mode = True

class Role(RoleInDBBase):
    pass

class RoleInDB(RoleInDBBase):
    pass
