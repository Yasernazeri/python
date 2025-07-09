from sqlalchemy.orm import Session
from todoapi.schema.todo import TodoCreate, TodoUpdate
from todoapi.models.db import engine
from todoapi.models.db import Todo



def create_todo_crud(item: TodoCreate, db:Session):
    todo = Todo(**item.model_dump())
    db.add(todo)
    db.commit()
    return todo



def show_all_todo_crud(db:Session):
    query = db.query(Todo).all()
    return query


def show_todo_by_id_crud(id, db:Session):
    query = db.query(Todo).where(Todo.id == id).first()
    return query


def upate_todo_crud(item:TodoUpdate, id, db:Session):
    todo = show_todo_by_id_crud(id, db)
    if item.model_dump().get("item"):
        a = db.query(Todo).where(Todo.id == id).update({Todo.title: item.title, Todo.completed: item.completed})
    else:
         a = db.query(Todo).where(Todo.id == id).update({Todo.completed: item.completed})

    db.commit()
    return a