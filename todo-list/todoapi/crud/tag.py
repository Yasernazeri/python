from sqlalchemy.orm import Session
from todoapi.schema.tag import TagCreate
from todoapi.models.db import engine
from todoapi.models.db import Tag


def create_tag_crud(data:TagCreate, db:Session):
    tag = Tag(**data.model_dump())
    db.add(tag)
    db.commit()
    return tag




def show_all_tag_crud(db:Session):
    query = db.query(Tag).all()
    return query



def show_tag_by_id_crud(id, db:Session):
    query = db.query(Tag).where(Tag.id == id).first()
    return query