from peewee import Model, BooleanField, BigIntegerField, DoesNotExist
from config.database import db
from fastapi import HTTPException


class BaseModel(Model):
    active = BooleanField(default=True)

    class Meta:
        database = db

    @classmethod
    def get_one(cls, id: int):
        data = cls.select().where(cls.id == id, cls.active).dicts()
        if list(data):
            return data.get()
        raise HTTPException(
            status_code=404, detail=f"{cls.__name__} not found"
        )

    @classmethod
    def get_list(cls):
        return list(cls.select().where(cls.active).dicts())

    @classmethod
    def update_one(cls, id: int, data_update: dict):
        try:
            query = cls.update(**data_update).where(
                cls.id == id
            )
            query.execute()

            data = cls.get_by_id(id)
            return data
        except DoesNotExist:
            raise HTTPException(
                status_code=404, detail=f"{cls.__name__} not found"
            )

    @classmethod
    def soft_delete(cls, id: int):
        try:
            data = cls.get_by_id(id)
            data.active = False
            data.save()
            return {"detail": f"Deleted {cls.__name__} {id}"}
        except DoesNotExist:
            raise HTTPException(
                status_code=404, detail=f"{cls.__name__} not found"
            )
