from typing import Any, Optional, List
from pydantic import BaseModel, EmailStr


class StudentSchemaBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    genre: Any
    priority: Any
    birth_date: Any
    is_active: bool = False

    class Config:
        orm_mode = True


class StudentSchemaCreate(StudentSchemaBase):
    password: str


class StudentSchemaUp(StudentSchemaBase):
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]
    password: Optional[str]
    genre: Optional[Any]
    is_active: Optional[bool]

