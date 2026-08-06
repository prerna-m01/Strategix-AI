from backend.app.database.base import Base
from backend.app.models import User


def test_user_table_exists():
    assert "users" in Base.metadata.tables