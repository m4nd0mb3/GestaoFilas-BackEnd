from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.student import StudentSchemaCreate, StudentSchemaUp, StudentSchemaBase
from db.session import get_db
from db.repository.student import create_new_student

router = APIRouter()


@router.post("/",response_model = StudentSchemaBase)
def create_student(user : StudentSchemaCreate,db: Session = Depends(get_db)):
    user = create_new_student(user=user,db=db)
    return user 