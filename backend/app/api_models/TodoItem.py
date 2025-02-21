from typing import Optional

from mongoengine import DynamicDocument, StringField, IntField
from pydantic import Field, BaseModel


class TodoItemModelIn(BaseModel):
    todo: str
    priority: Optional[int]

    class Config:
        orm_mode = True


class TodoItemModelOut(BaseModel):
    todo: str
    priority: int

    class Config:
        orm_mode = True


class TodoItem(DynamicDocument):
    todo = StringField()
    priority = IntField(default=2)

    # def to_dict(self) -> dict:
    #     return {
    #         "todo": self.todo,
    #         "priority": self.priority
    #     }

