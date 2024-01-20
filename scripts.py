import uvicorn


def start():
    uvicorn.run('PyUrl.backend.app:app', host="localhost", port=8000, reload=True)
