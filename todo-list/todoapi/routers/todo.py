from fastapi import APIRouter, Depends
from todoapi.schema.todo import TodoCreate, TodoShow, TodoUpdate
from typing import Annotated
from sqlalchemy.orm import Session
from todoapi.models.db import get_session
from todoapi.crud.todo import create_todo_crud, show_all_todo_crud, show_todo_by_id_crud, upate_todo_crud
from typing import List


router = APIRouter(prefix='/todo', tags=["todo"])



@router.get("/", response_model=List[TodoShow])
def show_all_todo(db:Annotated[Session, Depends(get_session)]):
    return show_all_todo_crud(db)




@router.get("/{id}", response_model=TodoShow)
def show_all_todo(id:int, db:Annotated[Session, Depends(get_session)]):
    return show_todo_by_id_crud(id, db)


@router.post("/", response_model=TodoShow)
def create_todo(item:TodoCreate, db:Annotated[Session, Depends(get_session)]):
    todo = create_todo_crud(item, db)
    return todo




@router.patch("/{id}")
def update_todo(id:int, item:TodoUpdate ,  db:Annotated[Session, Depends(get_session)]):
    upate_todo_crud(item, id, db)
    return "okko"