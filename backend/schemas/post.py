from schemas.base import Schema


class PostBase(Schema):
    title: str
    category: int
    content: str
    image: str = None


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    id: int