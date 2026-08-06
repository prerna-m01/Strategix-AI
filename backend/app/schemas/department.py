from pydantic import BaseModel, ConfigDict


class DepartmentBase(BaseModel):
    name: str
    description: str
    company_id: int


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentResponse(DepartmentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)