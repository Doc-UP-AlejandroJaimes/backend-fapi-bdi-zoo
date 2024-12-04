# app/models/animales.py
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database.database import Base

class Animales(Base):
    __tablename__ = "animales"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    fechanac = Column(Date, nullable=True)
    idcuidador = Column(Integer, ForeignKey("animals.CUIDADOR.ID"), nullable=False)
    idhabitat = Column(Integer, ForeignKey("animals.HABITAT.ID"), nullable=False)
    idespecie = Column(Integer, ForeignKey("animals.ESPECIE.ID"), nullable=False)
