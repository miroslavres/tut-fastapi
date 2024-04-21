from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .import models
from .database import  engine
# import routers file
from . routers import post, user, auth, vote
from .config import settings


print(settings.database_hostname)

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://www.google.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return{"message": "Hello world"}




