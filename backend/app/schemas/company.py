from pydantic import BaseModel, ConfigDict


class CompanyCreate(BaseModel):
    name: str
    industry: str
    headquarters: str
    ceo: str


class CompanyResponse(BaseModel):
    id: int
    name: str
    industry: str
    headquarters: str
    ceo: str

    model_config = ConfigDict(from_attributes=True)