import os
from typing import List

import uvicorn
from fastapi import FastAPI, HTTPException, APIRouter
from fastapi.params import Path
from mongoengine import connect
from starlette.middleware.cors import CORSMiddleware

from app.api_models.TodoItem import TodoItemModelIn, TodoItemModelOut, TodoItem

app = FastAPI()

router = APIRouter()

con = connect(db="todo", username=os.environ["MONGODB_USER"], password=os.environ["MONGODB_PW"],
              host=os.environ["MONGODB_CONNSTRING"])


@router.post("/{name}", status_code=201, description="Item has been created",
             response_model=TodoItemModelOut)
def create_item_prio_two(name: str = Path()):
    item = TodoItem(todo=name)
    item.save()
    # items.append(item)
    return TodoItemModelOut.from_orm(item)


@router.post("/", status_code=201, description="Item has been created",
             response_model=TodoItemModelOut)
def create_new_item(item: TodoItemModelIn):
    i = TodoItem(todo=item.todo, priority=item.priority)
    i.save()
    return item


@router.get("/", status_code=200, description="List all Items", response_model=List[TodoItemModelOut])
def get_all_items():
    items_db = TodoItem.objects
    return [TodoItemModelOut.from_orm(item) for item in items_db]


@router.get("/{itemid}")
def find_by_id(itemid: str = Path):
    if not itemid:
        raise HTTPException(status_code=400, detail="Invalid itemId supplied")
    for item in TodoItem.objects(todo=itemid):
        return TodoItemModelOut.from_orm(item)
    return HTTPException(status_code=404, detail="Item not found")


@router.delete("/{itemid}")
def delete_by_id(itemid: str = Path):
    if not itemid:
        raise HTTPException(status_code=400, detail="Invalid itemId supplied")
    items = TodoItem.objects(todo=itemid)
    if items:
        for item in items:
            item.delete()
        return None
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/")
def delete_item(item: TodoItemModelIn):
    items = TodoItem.objects(todo=item.todo, priority=item.priority).limit(1)
    for item in items:
        item.delete()
    return None


@router.put("/", response_model=TodoItemModelOut)
def update_todo(item: TodoItemModelIn):
    old_item = TodoItem.objects(todo=item.todo).limit(1).get(0)
    if old_item:
        old_item.priority = item.priority
        old_item.save()
        return TodoItemModelOut.from_orm(old_item)
    new_item = TodoItem(todo=item.todo, priority=item.priority)
    new_item.save()
    return TodoItemModelOut.from_orm(new_item)


app.include_router(router=router, prefix="/todos")

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])
