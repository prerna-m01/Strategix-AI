from fastapi import APIRouter

from backend.app.api.company import router as company_router
from backend.app.api.health import router as health_router

router = APIRouter()

router.include_router(health_router)
router.include_router(company_router)