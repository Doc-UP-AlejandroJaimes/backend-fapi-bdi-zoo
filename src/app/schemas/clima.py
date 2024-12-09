from pydantic import BaseModel

class ClimaBase(BaseModel):
    nombre: str

class ClimaCreate(ClimaBase):
    pass

class Clima(ClimaBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
