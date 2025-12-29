from fastapi import APIRouter
from models.Todo import Todo
from services.Todo_services import TodoServices


Todo_route = APIRouter(prefix = "/todos")

ts=TodoServices()

@Todo_route.post("/")
def add_todo(todo: Todo):
    return ts.add_todo(todo)

@Todo_route.get("")
def show_all_todos():
    return ts.show_all()

@Todo_route.get("/{id}")
def get_one_todo(id : int):
    return ts.get_one_todo(id)

@Todo_route.put("/{id}")
def update_todo(id : int , new_todo: Todo):
    return ts.update_todo(id,new_todo)

@Todo_route.delete("/{id}")
def delete_todo(id : int):
    return ts.delete_todo(id)