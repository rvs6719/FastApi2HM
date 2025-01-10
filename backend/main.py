# backend/main.py
from fastapi import FastAPI
from .routes import videos

app = FastAPI()

app.include_router(videos.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the YouTube Clone API!"}