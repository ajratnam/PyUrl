from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from .config import settings

engine = create_async_engine(settings.DATABASE_URL)
Session = async_sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()
