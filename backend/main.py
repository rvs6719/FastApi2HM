# backend/main.py
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .routes import videos

app = FastAPI()

app.include_router(videos.router)

# Обслуживание статических файлов
app.mount("/static", StaticFiles(directory="../frontend/build/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("../frontend/build/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)

@app.get("/{full_path:path}", response_class=HTMLResponse)
async def serve_spa(full_path: str):
    with open("../frontend/build/index.html") as f:
        return HTMLResponse(content=f.read(), status_code=200)