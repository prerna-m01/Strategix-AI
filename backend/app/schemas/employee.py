from datetime import date

from pydantic import BaseModel, ConfigDict, EmailStr


class EmployeeBase(BaseModel):
    employee_id: str
    full_name: str
    email: EmailStr
    department_id: int
    job_title: str
    location: str
    employment_type: str
    hire_date: date
    annual_salary: float


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeResponse(EmployeeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)