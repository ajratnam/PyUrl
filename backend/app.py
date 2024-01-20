from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Depends
from starlette.responses import RedirectResponse

from backend import models
from backend.crud import generate_random_code, create_url, get_url
from backend.database import engine, Session
from backend.schemas import ShortUrl, RequestUrl


@asynccontextmanager
async def connect_db(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(lifespan=connect_db)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


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
