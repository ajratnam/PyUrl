from pydantic import BaseModel


class RequestUrl(BaseModel):
    url: str
    code: str | None = None


class ShortUrl(BaseModel):
    url: str
    origin: str

    class Config:
        from_attributes = True


class ErrorResponse(BaseModel):
    detail: str
