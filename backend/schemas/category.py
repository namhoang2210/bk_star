from schemas.base import Schema


class CategoryBase(Schema):
    name: str
    description: str
    image: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    id: int
