from sqlalchemy.orm import Session

from schemas.employeer import EmployeerSchemaCreate
from db.models.employeer import EmployeerModel
from core.hashing import Hasher


def create_new_employeer(user:EmployeerSchemaCreate,db:Session):
    user = EmployeerModel(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        genre=user.genre,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_staff=False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user