from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from app.database.database import Base

class Habitat(Base):
    __tablename__ = "habitat"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    costobase = Column(Numeric(10, 2), nullable=True)
    idubicacion = Column(Integer, ForeignKey("animals.ubicacion.id"), nullable=False)
    idclima = Column(Integer, ForeignKey("animals.clima.id"), nullable=False)
    
    # Relación inversa opcional con Animales
    animales = relationship("Animales", back_populates="habitat")

    # Relación con `Ubicacion`
    ubicacion = relationship("Ubicacion", backref="habitat")
    # Relación con `Clima`
    clima = relationship("Clima", backref="habitat")
