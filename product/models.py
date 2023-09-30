from pydantic import BaseModel, Field

from backend.models import Model


class Category(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    parent: dict | None = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'name': 'Category',
                'description': 'Description',
                'parent': None
            }
        }


class MongoCategory(Model):
    class Meta:
        db = 'product'
        collection = 'category'


class Product(BaseModel):
    name: str = Field(...)
    price: float = Field(...)
    description: str = Field(...)
    count: int = Field(...)
    is_active: bool = Field(...)
    fields: dict = Field(...)

    class Config:
        schema_extra = {
            'example': {
                'name': 'Product',
                'price': 100.0,
                'description': 'Description',
                'count': 10,
                'is_active': True,
                'fields': {
                    'color': 'red',
                    'size': 'L'
                }
            }
        }


class MongoProduct(Model):
    class Meta:
        db = 'product'
        collection = 'product'
