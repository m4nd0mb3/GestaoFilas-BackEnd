from typing import Any, Optional, List
from pydantic import BaseModel, EmailStr


class EmployeerSchemaBase(BaseModel):
    user_name: str
    first_name: str
    last_name: str
    genre: Any
    is_active: bool = True
    is_staff: bool = False

    class Config:
        orm_mode = True


class EmployeerSchemaCreate(EmployeerSchemaBase):
    password: str


class EmployeerSchemaUp(EmployeerSchemaBase):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    genre: Optional[any]
    is_active: Optional[bool]
    is_staff: Optional[bool]

