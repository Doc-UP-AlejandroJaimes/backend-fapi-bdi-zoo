from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Ubicacion(Base):
    __tablename__ = "ubicacion"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
