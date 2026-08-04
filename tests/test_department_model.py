from backend.app.models import Department


def test_department_table():
    assert Department.__tablename__ == "departments"