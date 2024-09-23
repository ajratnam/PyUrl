import requests
from requests import Response

API_URL = "http://localhost:8000"


def shorten_url(origin_url: str, custom_code: str | None = None) -> dict:
    payload = {"url": origin_url}
    if custom_code:
        payload["code"] = custom_code
    response = requests.post(f"{API_URL}/shorten", json=payload)
    return response.json()


def get_url_info(code: str) -> Response:
    response = requests.get(f"{API_URL}/info/{code}")
    return response.json()


def redirect_url(code: str) -> Response:
    response = requests.get(f"{API_URL}/{code}")
    return response
