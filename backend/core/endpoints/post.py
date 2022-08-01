from fastapi import APIRouter
from schemas.post import PostCreate,PostUpdate
from models.post import Post


router = APIRouter()


@router.get('/')
def get_post():
    return Post.get_list()


@router.get('/{id}')
def get_one(id: int):
    return Post.get_one(id)


@router.post('/')
def create_post(new_post: PostCreate):
    post = Post.create(**new_post.dict())
    return post


@router.put('/')
def create_post(new_post: PostUpdate):
    post = Post.update_one(new_post.id, new_post.dict())
    return post

@router.get('/category/{category}')
def get_list_by_category(category: int):
    return Post.get_posts_by_category(category)
