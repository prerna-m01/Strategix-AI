from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app.auth.jwt import create_access_token
from backend.app.database.session import get_db
from backend.app.schemas.auth import LoginRequest, TokenResponse
from backend.app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=TokenResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    service = UserService(db)

    user = service.authenticate_user(
        request.email,
        request.password,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
    }