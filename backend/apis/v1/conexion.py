from fastapi import APIRouter, Response, status

router = APIRouter()


# GET current user
@router.get('/')
def is_online():
    return Response(status_code=status.HTTP_200_OK)
