from fastapi import APIRouter, Depends
from utils.auth import Auth

router = APIRouter()


@router.get("/")
def index(data=Depends(Auth())):
    return {
        "Hello": "test api"
    }
