from pydantic import BaseModel,EmailStr
from datetime import datetime

from app.database import Base

class PostBase(BaseModel):
    title: str
    content: str
    published : bool = True

class PostCreate(PostBase):
    pass

class Post(BaseModel):
    id :int
    created_at: datetime
    class Config:
         orm_mode =True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class User_res(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
         orm_mode =True