from backend.app.models.employee import Employee


def test_employee_table():
    assert Employee.__tablename__ == "employees"