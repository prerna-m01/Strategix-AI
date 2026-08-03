from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "project": "Strategix AI",
        "version": "0.1.0",
    }