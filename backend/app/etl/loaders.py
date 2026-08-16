from sqlalchemy.orm import Session

from backend.app.models.employee import Employee


def load_employees(
    db: Session,
    records: list[dict],
) -> int:
    employees = []

    for record in records:
        employee = Employee(
            employee_id=record["employee_id"],
            full_name=record["full_name"],
            email=record["email"],
            department_id=record["department_id"],
            job_title=record["job_title"],
            location=record["location"],
            employment_type=record["employment_type"],
            hire_date=record["hire_date"],
            annual_salary=record["annual_salary"],
        )

        employees.append(employee)

    if not employees:
        return 0

    db.add_all(employees)
    db.commit()

    return len(employees)