from pydantic import BaseModel, ConfigDict


class BusinessKPIBase(BaseModel):
    metric_name: str
    metric_value: float
    unit: str
    year: int
    department_id: int


class BusinessKPICreate(BusinessKPIBase):
    pass


class BusinessKPIResponse(BusinessKPIBase):
    id: int

    model_config = ConfigDict(from_attributes=True)