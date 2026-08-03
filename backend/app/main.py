from fastapi import FastAPI

from backend.app.api.router import router
from backend.app.config.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Strategix AI",
        "version": settings.APP_VERSION,
    }