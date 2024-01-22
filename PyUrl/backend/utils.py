import os
import random
import string

from .models import Url
from .schemas import ShortUrl

random_chars = string.ascii_letters + string.digits


def random_code(length: int) -> str:
    return "".join(random.choices(random_chars, k=length))


def convert(url: Url | None) -> ShortUrl | None:
    if isinstance(url, Url):
        short_url = f"http://localhost:8000/{url.code}"
        return ShortUrl(url=short_url, origin=url.origin)


def get_path(file: str) -> str:
    file_path = os.path.abspath(file)
    relative_path = os.path.relpath(file_path, start=os.getcwd())
    module_path = os.path.splitext(relative_path)[0]
    return module_path.replace(os.path.sep, ".")
