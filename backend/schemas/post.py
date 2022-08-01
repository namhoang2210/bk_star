from schemas.base import Schema


class PostBase(Schema):
    title: str
    category_id: int
    content: str
    image: str


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    id: int