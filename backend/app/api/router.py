from fastapi import APIRouter

from backend.app.api.auth import router as auth_router
from backend.app.api.business_kpi import router as business_kpi_router
from backend.app.api.company import router as company_router
from backend.app.api.department import router as department_router
from backend.app.api.health import router as health_router


router = APIRouter(
    prefix="/api/v1",
)

router.include_router(health_router)
router.include_router(auth_router)
router.include_router(company_router)
router.include_router(department_router)
router.include_router(business_kpi_router)