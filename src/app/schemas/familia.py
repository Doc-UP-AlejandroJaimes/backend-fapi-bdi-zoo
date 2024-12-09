from pydantic import BaseModel

class FamiliaBase(BaseModel):
    nombrecientifico: str
    nombrecomun: str

class FamiliaCreate(FamiliaBase):
    pass

class Familia(FamiliaBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
