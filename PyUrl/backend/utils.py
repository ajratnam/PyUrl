import os
import secrets
import string
from pathlib import Path

from .models import Url
from .schemas import ShortUrl

random_chars = string.ascii_letters + string.digits


def random_code(length: int) -> str:
    return "".join(secrets.choice(random_chars) for _ in range(length))


def convert(url: Url | None) -> ShortUrl | None:
    if isinstance(url, Url):
        short_url = f"http://localhost:8000/{url.code}"
        return ShortUrl(url=short_url, origin=url.origin)
    return None


def get_path(file: str) -> str:
    file_path = Path(file).resolve()
    relative_path = file_path.relative_to(Path.cwd())
    module_path = relative_path.parent / relative_path.stem
    return str(module_path).replace(os.path.sep, ".")
