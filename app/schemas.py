from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from typing_extensions import Annotated



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    


class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: str

    class Config:
        orm_mode = True


class Post(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int


class UserCreate(BaseModel):
    email: EmailStr
    password: str






class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int    
    dir: Annotated[int, Field(strict=True, le=1)] # aji je 1 onda se dodaje post i provera se radi da li je vec glasao ako se stavi nula u slanju radi delete glasanja
    #user_id: int