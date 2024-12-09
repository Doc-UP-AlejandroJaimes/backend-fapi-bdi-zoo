from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal
from typing import Optional
from app.schemas.especialidad import Especialidad

class CuidadorBase(BaseModel):
    nombre: str | None
    fechacontratacion: date | None
    salario: Decimal  | None
    idespecialidad: int | None

class CuidadorCreate(CuidadorBase):
    pass

class CuidadorUpdate(BaseModel):
    nombre: Optional[str] | None
    fechacontratacion: Optional[date] | None
    salario: Optional[Decimal]  | None
    idespecialidad: Optional[int] | None

class CuidadorSchema(CuidadorBase):
    id: int
    especialidad: Especialidad

class CuidadorAnimal(BaseModel):
    id: int
    nombre: str | None
    especialidad: Especialidad

    class Config:
        from_attributes = True  # Habilitar mapeo desde modelos SQLAlchemy
        populate_by_name = True  # Usa nombres internos si es necesario