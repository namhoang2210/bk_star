from fastapi import APIRouter
from schemas.category import CategoryCreate, CategoryUpdate
from models.category import Category


router = APIRouter()


@router.get('/')
def get_category():
    return Category.get_list()


@router.post('/')
def create_category(new_category: CategoryCreate):
    category = Category.create(**new_category.dict())
    return category


@router.put('/')
def create_category(new_category: CategoryUpdate):
    category = Category.update_one(new_category.id, new_category.dict())
    return category
