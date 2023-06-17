from fastapi import FastAPI

from src.core.config import settings
from src.api.base import router

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
    app.include_router(router)
    return app 

app = start_application()

