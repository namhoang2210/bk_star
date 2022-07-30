from models.base import BaseModel
from peewee import CharField


class Post(BaseModel):
    name = CharField()

    class Meta:
        db_table = 'post'