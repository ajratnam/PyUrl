from sqlalchemy.ext.asyncio import AsyncSession

from .models import Url
from .schemas import RequestUrl, ShortUrl
from .utils import convert, random_code


async def add[T](db: AsyncSession, obj: T) -> T:
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_url(db: AsyncSession, code: str) -> ShortUrl | None:
    return convert(await db.get(Url, code))


async def create_url(db: AsyncSession, request: RequestUrl) -> ShortUrl:
    if await get_url(db, request.code):
        raise ValueError("Code already exists")

    url = Url(code=request.code, origin=request.url)
    return convert(await add(db, url))


async def generate_random_code(db: AsyncSession, length: int) -> str:
    while code := random_code(length):
        if not await get_url(db, code):
            return code
