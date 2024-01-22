# PyUrl
Url shortening service written in Python

### Install dependencies
```bash
poetry install
```

### Apply all migrations
```bash
albemic upgrade head
```

### Run the backend
```bash
poetry run server
```

### Run the backend in development mode
```bash
uvicorn PyUrl.backend.app:app --reload
```
