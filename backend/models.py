from sqlalchemy import Column, String

from .database import Base


class Url(Base):
    __tablename__ = "urls"

    code = Column(String, primary_key=True)
    origin = Column(String)
