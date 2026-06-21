from pydantic import BaseModel
from typing import Optional


class PostModel(BaseModel):
    id: int
    userId: int
    title: str
    body: str


class CreatePostModel(BaseModel):
    title: str
    body: str
    userId: int