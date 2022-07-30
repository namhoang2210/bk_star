from fastapi import APIRouter, Depends
from utils.auth import Auth
from core.endpoints import (
    test,
    category,
    post
)

api_router = APIRouter()

api_router.include_router(
    test.router,
    prefix="/test",
    tags=["test"],
    dependencies=[Depends(Auth)]
)
api_router.include_router(
    category.router,
    prefix="/category",
    tags=["category"]
)
api_router.include_router(
    category.router,
    prefix="/post",
    tags=["post"]
)
