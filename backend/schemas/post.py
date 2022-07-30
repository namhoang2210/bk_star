from schemas.base import Schema


class PostBase(Schema):
    name: str


class CategoryCreate(PostBase):
    pass


class CategoryUpdate(PostBase):
    id: int