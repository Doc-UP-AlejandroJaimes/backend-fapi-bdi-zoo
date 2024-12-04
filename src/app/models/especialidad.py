from sqlalchemy import Column, Integer, String
from app.database.database import Base

class Especialidad(Base):
    __tablename__ = "especialidad"
    __table_args__ = {"schema": "animals"}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
