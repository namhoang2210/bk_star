from fastapi import APIRouter
from schemas.post import PostCreate, PostUpdate
from models.post import Post


router = APIRouter()


@router.get('/')
def get_post():
    return Post.get_list()


@router.post('/')
def create_post(new_post: PostCreate):
    post = Post.create(**new_post.dict())
    return post


@router.put('/')
def create_post(new_post: PostUpdate):
    post = Post.update_one(new_post.id, new_post.dict())
    return post
