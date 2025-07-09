from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String, Integer, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
     pass



class Tag(Base):
     __tablename__ = "tag"
     id:Mapped[int] = mapped_column(Integer, primary_key=True)
     title:Mapped[str] = mapped_column(String(50))
     todos:Mapped[List["Todo"]] = relationship(back_populates='tag', cascade="all, delete-orphan")



class Todo(Base):
     __tablename__ = "todo"
     id:Mapped[int] = mapped_column(Integer, primary_key=True)
     title:Mapped[str] = mapped_column(String(50))
     completed:Mapped[bool] = mapped_column(Boolean, default=False)
     created:Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
     tag_id:Mapped[int] = mapped_column(ForeignKey("tag.id"))
     tag:Mapped[Tag] = relationship(back_populates="todos")




engine = create_engine("sqlite:///todo.db", echo=True)



def get_session():
    with Session(engine) as session:
        yield session