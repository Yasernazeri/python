from fastapi import APIRouter, Depends
from todoapi.schema.tag import TagCreate, TagShow
from todoapi.crud.tag import create_tag_crud, show_all_tag_crud, show_tag_by_id_crud
from typing import Annotated
from todoapi.models.db import get_session
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(prefix="/tag", tags=["tag"])

from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    full_name: Optional[str] = None
    password: str



def get_answer():
    return "hello"



@router.post("/create")
def create_tag_router(data:TagCreate, txt:Annotated[str, Depends(get_answer)]):
    tag  = create_tag_crud(data)
    print(txt)
    return "ok"


@router.get("/all")
def get_all():
    return {"msg": "all todos"}






@router.post("/create", response_model=TagShow)
def create_tag_router(data:TagCreate, db:Annotated[Session, Depends(get_session)]):
    tag  = create_tag_crud(data, db)
    return tag




@router.get("/show", response_model=List[TagShow])
def show_tag_router(db:Annotated[Session, Depends(get_session)]):
    return show_all_tag_crud(db)



@router.get("/show/{id}")
def show_tag_router(id:int, db:Annotated[Session, Depends(get_session)]):
    tag = show_tag_by_id_crud(id, db)
    if tag:
        return TagShow(id=tag.id, title=tag.title)
    else:
        return {"msg": "not found"}