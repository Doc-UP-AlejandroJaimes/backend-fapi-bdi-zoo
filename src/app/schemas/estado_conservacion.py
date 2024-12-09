from pydantic import BaseModel

class EstadoConservacionBase(BaseModel):
    codigo: str
    nombre: str
    descripcion: str

class EstadoConservacionCreate(EstadoConservacionBase):
    pass

class EstadoConservacion(EstadoConservacionBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
