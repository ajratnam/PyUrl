# PyUrl
Url shortening service written in Python

### Install dependencies
```bash
poetry install
```

### Apply all migrations
```bash
alembic upgrade head
```

### Run backend using docker
```bash
docker-compose up
```

### Run the backend
```bash
poetry run server
```

### Run the backend in development mode
```bash
uvicorn PyUrl.backend.app:app --reload
````

### Install development dependencies
```bash
poetry install --dev
```

### Run code formatter
```bash
pre-commit run --all-files
```

### Install pre-commit hooks
```bash
pre-commit install
```

### Run the code formatter
```bash
ruff --fix .
```

### Create a new migration
```bash
alembic revision --autogenerate -m "Migration message"
```