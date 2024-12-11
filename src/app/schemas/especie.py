from pydantic import BaseModel
from typing import Optional
from app.schemas.familia import Familia
from app.schemas.estado_conservacion import EstadoConservacion

class EspecieBase(BaseModel):
    nombre: str
    idfamilia: int
    idestadoconservacion: int

class EspecieCreate(EspecieBase):
    pass

class Especie(EspecieBase):
    id: int

class EspecieAnimal(BaseModel):
    id: int
    nombre: str
    familia: Optional[Familia]
    estado_conservacion: Optional[EstadoConservacion]

    class Config:
        from_attributes = True
        populate_by_name = True

class EspecieDropDown(BaseModel):
    id: int
    nombre: str
    class Config:
        from_attributes = True
