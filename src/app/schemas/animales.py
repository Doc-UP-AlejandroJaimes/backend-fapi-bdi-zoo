# app/schemas/animales.py
from pydantic import BaseModel
from datetime import date

class AnimalesBase(BaseModel):
    nombre: str
    fechanac: date | None
    idcuidador: int | None
    idhabitat: int | None
    idespecie: int | None

class AnimalesCreate(AnimalesBase):
    pass

class Animales(AnimalesBase):
    id: int

    class Config:
        from_attributes = True
