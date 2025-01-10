# backend/models.py
from pydantic import BaseModel
from typing import List, Optional

class Author(BaseModel):
    id: int
    name: str
    subscribers: int

class Comment(BaseModel):
    id: int
    video_id: int
    author: str
    content: str

class Video(BaseModel):
    id: int
    title: str
    author: Author
    views: int
    likes: int
    comments: List[Comment]

class RecommendedVideo(BaseModel):
    id: int
    title: str
    author: Author
    views: int
    preview_url: str