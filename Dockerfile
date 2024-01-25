FROM python:3.12-slim-bookworm

WORKDIR /app

ENV POETRY_CACHE_DIR='/tmp/poetry_cache' \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.7.1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

ADD pyproject.toml poetry.lock /app/

RUN pip install poetry
RUN poetry install --no-dev --no-root --no-ansi && rm -rf $POETRY_CACHE_DIR

ADD . /app

EXPOSE 8000

CMD ["alembic", "upgrade", "head"]
CMD ["uvicorn", "PyUrl.backend.app:app", "--host", "0.0.0.0", "--port", "8000"]