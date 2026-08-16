from fastapi import FastAPI

from backend.app.api.router import router as api_router
from backend.app.config.settings import settings
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
from backend.app.core.logger import logger


logger.info("Strategix AI Started Successfully")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG,
)


# ============================================================
# Exception Handlers
# ============================================================

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


# ============================================================
# API Routes
# ============================================================

app.include_router(api_router)


# ============================================================
# Root Endpoint
# ============================================================

@app.get("/")
async def root():
    return {
        "message": "Welcome to Strategix AI",
        "version": settings.APP_VERSION,
    }