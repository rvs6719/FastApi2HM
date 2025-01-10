# backend/routers/videos.py
from fastapi import APIRouter, HTTPException
from typing import List
from ..models import Video, RecommendedVideo, Comment

router = APIRouter()

fake_videos_db = [
    {
        "id": 1,
        "title": "Sample Video 1",
        "author": {"id": 1, "name": "Author 1", "subscribers": 1000},
        "views": 5000,
        "likes": 100,
        "comments": [{"id": 1, "video_id": 1, "author": "User1", "content": "Great video!"}]
    },
    {
        "id": 2,
        "title": "Sample Video 2",
        "author": {"id": 2, "name": "Author 2", "subscribers": 2000},
        "views": 3000,
        "likes": 50,
        "comments": [{"id": 2, "video_id": 2, "author": "User2", "content": "Nice video!"}]
    }
]

fake_recommended_videos_db = [
    {
        "id": 3,
        "title": "Recommended Video 1",
        "author": {"id": 3, "name": "Author 3", "subscribers": 1500},
        "views": 2000,
        "preview_url": "https://example.com/preview1.jpg"
    },
    {
        "id": 4,
        "title": "Recommended Video 2",
        "author": {"id": 4, "name": "Author 4", "subscribers": 2500},
        "views": 2500,
        "preview_url": "https://example.com/preview2.jpg"
    }
]

@router.get("/videos/", response_model=List[Video])
async def read_videos():
    return fake_videos_db

@router.get("/videos/{video_id}", response_model=Video)
async def read_video(video_id: int):
    for video in fake_videos_db:
        if video["id"] == video_id:
            return video
    raise HTTPException(status_code=404, detail="Video not found")

@router.get("/recommended/", response_model=List[RecommendedVideo])
async def read_recommended_videos():
    return fake_recommended_videos_db

@router.post("/videos/{video_id}/comments/", response_model=Comment)
async def add_comment(video_id: int, comment: Comment):
    for video in fake_videos_db:
        if video["id"] == video_id:
            comment.id = len(video["comments"]) + 1
            video["comments"].append(comment)
            return comment
    raise HTTPException(status_code=404, detail="Video not found")