from fastapi import APIRouter
from sqlalchemy import text

from backend.app.database.session import SessionLocal

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    db = SessionLocal()

    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    finally:
        db.close()