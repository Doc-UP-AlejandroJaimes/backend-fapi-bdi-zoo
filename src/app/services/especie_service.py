# app/services/animales_service.py
from sqlalchemy.orm import Session
from app.models.especie import Especie as EspecieModel
from app.schemas.especie import EspecieDropDown
from fastapi import HTTPException


def get_especies(db: Session):
    """
    Servicio para obtener las especies.
    """
    especies = db.query(EspecieModel).all()

    return {
        "results": [EspecieDropDown.from_orm(especie) for especie in especies]
    }