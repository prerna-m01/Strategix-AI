from fastapi import Request
from fastapi.responses import JSONResponse

from backend.app.core.exceptions import (
    DuplicateResourceException,
    ResourceNotFoundException,
    ValidationException,
)


async def resource_not_found_handler(
    request: Request,
    exc: ResourceNotFoundException,
):
    return JSONResponse(
        status_code=404,
        content={
            "detail": f"{exc.resource} not found"
        },
    )


async def duplicate_resource_handler(
    request: Request,
    exc: DuplicateResourceException,
):
    return JSONResponse(
        status_code=409,
        content={
            "detail": f"{exc.resource} already exists"
        },
    )


async def validation_handler(
    request: Request,
    exc: ValidationException,
):
    return JSONResponse(
        status_code=400,
        content={
            "detail": exc.message
        },
    )