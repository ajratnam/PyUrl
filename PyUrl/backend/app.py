from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException, Depends
from starlette.responses import RedirectResponse

from .crud import generate_random_code, create_url, get_url
from .database import engine, Session
from .schemas import ShortUrl, RequestUrl
from .utils import get_path


@asynccontextmanager
async def connect_db(_: FastAPI):
    yield
    await engine.dispose()


app = FastAPI(lifespan=connect_db)


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        await db.close()


@app.post("/shorten", response_model=ShortUrl)
async def shorten_url(request: RequestUrl, db: Session = Depends(get_db)):
    request.code = request.code or await generate_random_code(db, 6)
    try:
        return await create_url(db, request)
    except ValueError:
        raise HTTPException(status_code=409, detail="Code already exists")


@app.get("/info/{code}", response_model=ShortUrl)
async def info(code: str, db: Session = Depends(get_db)):
    if short_url := await get_url(db, code):
        return short_url
    raise HTTPException(status_code=404, detail="URL not found")


@app.get("/{code}")
async def redirect(code: str, db: Session = Depends(get_db)):
    if short_url := await get_url(db, code):
        return RedirectResponse(url=short_url.origin)
    raise HTTPException(status_code=404, detail="URL not found")


def start_server():
    path = get_path(__file__)
    uvicorn.run(f"{path}:app")


if __name__ == "__main__":
    start_server()
