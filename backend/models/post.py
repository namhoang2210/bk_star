from models.base import BaseModel
from peewee import (
    CharField,
    IntegerField,
    ForeignKeyField,
    fn,
    JOIN
)
from models.category import Category


class Post(BaseModel):
    title = CharField()
    category = ForeignKeyField(Category, column_name='category_id')
    content = CharField()
    image = CharField()

    class Meta:
        db_table = 'post'

    @classmethod
    def get_posts_by_category(cls, category_id):
        posts = (
            cls.select(
                cls.id,
                Category.name,
                cls.image,
                cls.title,
                cls.content
            ).join(
                Category, JOIN.LEFT_OUTER, on=Category.id == cls.category
            ).where(
                Category.active, cls.active
            ).dicts()
        )
        return list(posts)