from fastapi import FastAPI

from backend.app.api.router import router
from backend.app.config.settings import settings
from backend.app.core.logger import logger

from backend.app.core.exceptions import (
    DuplicateResourceException,
    ResourceNotFoundException,
    ValidationException,
)

from backend.app.core.handlers import (
    duplicate_resource_handler,
    resource_not_found_handler,
    validation_handler,
)

logger.info("Strategix AI Started Successfully")
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)

app.add_exception_handler(
    ResourceNotFoundException,
    resource_not_found_handler,
)

app.add_exception_handler(
    DuplicateResourceException,
    duplicate_resource_handler,
)

app.add_exception_handler(
    ValidationException,
    validation_handler,
)

app.include_router(router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to Strategix AI",
        "version": settings.APP_VERSION,
    }