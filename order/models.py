from pydantic import BaseModel, Field

from account.models import User
from backend.models import Model


class Cart(BaseModel):
    product: dict = Field(...)
    quantity: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "product": {
                    "id": "1",
                    "name": "Test",
                    "price": 10.0
                },
                "quantity": 1
            }
        }


class Order(BaseModel):
    customer: User = Field(...)
    carts: list[Cart] = Field(...)
    description: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "customer": {
                    "id": "1",
                    "name": "John Doe",
                    "email": "test@test.com"
                },
                "carts": [
                    {
                        "product": {
                            "id": "1",
                            "name": "Test",
                            "price": 10.0
                        },
                        "quantity": 1
                    }
                ],
                "description": "Test"
            }
        }


class MongoOrder(Model):
    class Meta:
        collection = 'orders'
        db = 'order'
