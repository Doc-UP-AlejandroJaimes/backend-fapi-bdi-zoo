# app/models/cuidador.py
from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base

class Cuidador(Base):
    __tablename__ = "cuidador"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    fechacontratacion = Column(Date, nullable=False)
    salario = Column(Numeric(10, 2), nullable=False)
    idespecialidad = Column(Integer, ForeignKey("animals.especialidad.id"), nullable=False)

    # Relación con `Especialidad`
    especialidad = relationship("Especialidad", backref="cuidadores")