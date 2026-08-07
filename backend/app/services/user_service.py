from sqlalchemy.orm import Session

from backend.app.auth.hashing import verify_password
from backend.app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def authenticate_user(
        self,
        email: str,
        password: str,
    ):
        user = self.repository.get_by_email(email)

        if not user:
            return None

        if not verify_password(
            password,
            user.hashed_password,
        ):
            return None

        return user