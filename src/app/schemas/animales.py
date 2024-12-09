# app/schemas/animales.py
from pydantic import BaseModel
from datetime import date
from typing import Optional
from app.schemas.cuidador import CuidadorAnimal
from app.schemas.especie import EspecieAnimal
from app.schemas.habitat import HabitatAnimal

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
        arbitrary_types_allowed = True

class AnimalesGetEndpoint(BaseModel):
    id: int
    nombre: str
    fechanac: date | None
    cuidador: Optional[CuidadorAnimal]
    especie: Optional[EspecieAnimal]
    habitat: Optional[HabitatAnimal]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True



    