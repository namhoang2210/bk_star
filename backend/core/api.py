from fastapi import APIRouter, Depends
from utils.auth import Auth
from core.endpoints import (
    test
)

api_router = APIRouter()

api_router.include_router(
    test.router,
    prefix="/test",
    tags=["test"],
    dependencies=[Depends(Auth)]
)
