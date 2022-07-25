from schemas.base import Schema


class CategoryBase(Schema):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    id: int
