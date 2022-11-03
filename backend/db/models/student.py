from sqlalchemy import Column,Integer, String,Boolean, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship

from db.base_class import Base

import enum

class GenreEnum(enum.Enum):
    male = 1
    female = 2

class PriorityEnum(enum.Enum):
    normal = 1
    old_person = 2
    pregnant = 3
    deficient = 4

class StudentModel(Base):
    username = Column(String,primary_key=True,nullable=False,unique=True,index=True)
    password = Column(String,nullable=False)
    first_name = Column(String,unique=True,nullable=False)
    last_name = Column(String,unique=True,nullable=False)
    genre = Column(Enum(GenreEnum), nullable=False)
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.normal, nullable=False)
    birth_date = Column(Date(), nullable=False)
    is_active = Column(Boolean(),default=True)