from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from app.schemas.clima import Clima
from app.schemas.ubicacion import Ubicacion

class HabitatBaseModel(BaseModel):
    nombre: str
    idubicacion: int
    idclima: int
    costobase: Decimal
    pass

class Habitat(HabitatBaseModel):
    id: int

class HabitatAnimal(BaseModel):
    id: int
    nombre: str
    clima: Optional[Clima]
    ubicacion: Optional[Ubicacion]
    
    class Config:
        from_attributes = True
        
