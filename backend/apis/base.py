from fastapi import APIRouter
from apis.v1 import conexion
from apis.v1.endpoints import student, employeer


api_router = APIRouter()
api_router.include_router(student.router,prefix="/students",tags=["students"])
api_router.include_router(student.router,prefix="/employeers",tags=["employeers"])
api_router.include_router(conexion.router)