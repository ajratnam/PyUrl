from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .config import settings

engine = create_async_engine(settings.DATABASE_URL)
Session = async_sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()
