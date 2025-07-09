from fastapi import FastAPI
from todoapi.routers.tag import router as tagRouter
from todoapi.routers.todo import router as todoRouter
from todoapi.models.db import Base
from todoapi.models.db import engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost:5173"
]
@app.on_event('startup')
def lifeSpan():
    Base.metadata.create_all(engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tagRouter)
app.include_router(todoRouter)

@app.get("/main")
def ping():
    return {"msg": "pong"}
