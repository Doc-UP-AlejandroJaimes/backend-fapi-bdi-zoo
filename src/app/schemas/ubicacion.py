from pydantic import BaseModel

class UbicacionBase(BaseModel):
    nombre: str

class UbicacionCreate(UbicacionBase):
    pass

class Ubicacion(UbicacionBase):
    id: int

    class Config:
        from_attributes = True
        populate_by_name = True
