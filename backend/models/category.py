from models.base import BaseModel
from peewee import CharField


class Category(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'category'

