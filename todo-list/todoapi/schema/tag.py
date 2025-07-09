from pydantic import BaseModel


class TagCreate(BaseModel):
    title:str
    

class TagShow(BaseModel):
    id:int
    title:str
    