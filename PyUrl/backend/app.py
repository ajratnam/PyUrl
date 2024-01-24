from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from starlette.responses import RedirectResponse

from .crud import create_url, generate_random_code, get_url
from .database import Session, engine
from .schemas import RequestUrl, ShortUrl
from .utils import get_path


@asynccontextmanager
async def connect_db(_: FastAPI) -> AsyncIterator[None]:
    yield
    await engine.dispose()


app = FastAPI(lifespan=connect_db)


async def get_db() -> AsyncIterator[Session]:
    db = Session()
    try:
        yield db
    finally:
        await db.close()


deps = Depends(get_db)


@app.post("/shorten", response_model=ShortUrl)
async def shorten_url(request: RequestUrl, db: Session = deps) -> ShortUrl:
    request.code = request.code or await generate_random_code(db, 6)
    try:
        return await create_url(db, request)
    except ValueError:
        raise HTTPException(status_code=409, detail="Code already exists") from None


@app.get("/info/{code}", response_model=ShortUrl)
async def info(code: str, db: Session = deps) -> ShortUrl:
    if short_url := await get_url(db, code):
        return short_url
    raise HTTPException(status_code=404, detail="URL not found")


@app.get("/{code}")
async def redirect(code: str, db: Session = deps) -> RedirectResponse:
    if short_url := await get_url(db, code):
        return RedirectResponse(url=short_url.origin)
    raise HTTPException(status_code=404, detail="URL not found")


def start_server() -> None:
    path = get_path(__file__)
    uvicorn.run(f"{path}:app")


if __name__ == "__main__":
    start_server()
