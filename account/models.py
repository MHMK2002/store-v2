from pydantic import BaseModel, Field

from backend.models import Model


class User(BaseModel):
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: str = Field(pattern='^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    password: str = Field()
    is_active: bool = Field(...)
    is_staff: bool = Field(...)
    is_superuser: bool = Field(...)
    is_blocked: bool = Field(...)
    is_deleted: bool = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'first_name': 'John',
                'last_name': 'Doe',
                'email': 'john@gmail.com',
                'password': 'password',
                'is_active': True,
                'is_staff': False,
                'is_superuser': False,
                'is_blocked': False,
                'is_deleted': False
            }
        }


class MongoUser(Model):
    class Meta:
        db = 'account'
        collection = 'user'
