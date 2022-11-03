from sqlalchemy.orm import Session

from schemas.student import StudentSchemaCreate
from db.models.student import StudentModel
from core.hashing import Hasher


def create_new_student(user:StudentSchemaCreate,db:Session):
    user = StudentModel(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        genre=user.genre,
        birth_date=user.birth_date,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user