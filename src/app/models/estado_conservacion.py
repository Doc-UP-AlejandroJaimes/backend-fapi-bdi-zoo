from sqlalchemy import Column, Integer, String
from app.database.database import Base

class EstadoConservacion(Base):
    __tablename__ = "estado_conservacion"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(2), nullable=False)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(50), nullable=False)