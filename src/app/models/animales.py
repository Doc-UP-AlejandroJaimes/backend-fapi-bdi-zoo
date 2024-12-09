from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Animales(Base):
    __tablename__ = "animales"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    fechanac = Column(Date, nullable=True)
    idcuidador = Column(Integer, ForeignKey("animals.cuidador.id"), nullable=False)
    idhabitat = Column(Integer, ForeignKey("animals.habitat.id"), nullable=False)
    idespecie = Column(Integer, ForeignKey("animals.especie.id"), nullable=False)

    cuidador = relationship("Cuidador", back_populates="animales")
    habitat = relationship("Habitat", back_populates="animales")
    especie = relationship("Especie", back_populates="animales")
