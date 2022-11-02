from sqlalchemy import Column,Integer, String,Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship

from db.base_class import Base

import enum

class GenreEnum(enum.Enum):
    male = 1
    female = 2

class EmployeerModel(Base):
    username = Column(String,primary_key=True,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)
    first_name = Column(String,unique=True,nullable=False)
    last_name = Column(String,unique=True,nullable=False)
    genre = Column(Enum(GenreEnum), nullable=False)
    is_active = Column(Boolean(),default=True)
    is_staff = Column(Boolean(),default=False)