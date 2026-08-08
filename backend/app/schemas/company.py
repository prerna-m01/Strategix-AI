from pydantic import BaseModel, ConfigDict, Field


class CompanyCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    industry: str = Field(..., min_length=1, max_length=255)
    headquarters: str = Field(..., min_length=1, max_length=255)
    ceo: str = Field(..., min_length=1, max_length=255)


class CompanyUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    industry: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    headquarters: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )

    ceo: str | None = Field(
        default=None,
        min_length=1,
        max_length=255,
    )


class CompanyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    industry: str
    headquarters: str
    ceo: str