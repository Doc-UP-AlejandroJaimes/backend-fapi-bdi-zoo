from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Especie(Base):
    __tablename__ = "especie"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    idfamilia = Column(Integer, ForeignKey("animals.familia.id"), nullable=False)
    idestadoconservacion = Column(Integer, ForeignKey("animals.estado_conservacion.id"), nullable=False)

    # Relación inversa explícita
    animales = relationship("Animales", back_populates="especie")

    # Relación con `Familia`
    familia = relationship("Familia", backref="especie")
    # Relación con `EstadoConservacion`
    estado_conservacion = relationship("EstadoConservacion", backref="especie")