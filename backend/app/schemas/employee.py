from datetime import date

from pydantic import BaseModel, ConfigDict


class EmployeeCreate(BaseModel):
    employee_id: str
    full_name: str
    email: str
    department_id: int
    job_title: str
    location: str
    employment_type: str
    hire_date: date
    annual_salary: float


class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    full_name: str
    email: str
    department_id: int
    job_title: str
    location: str
    employment_type: str
    hire_date: date
    annual_salary: float

    model_config = ConfigDict(from_attributes=True)