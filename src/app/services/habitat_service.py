# app/services/animales_service.py
from sqlalchemy.orm import Session
from app.models.habitat import Habitat as HabitatModel
from app.schemas.habitat import HabitatDropDown
from fastapi import HTTPException


def get_habitats(db: Session):
    """
    Servicio para obtener los habitats.
    """
    habitats = db.query(HabitatModel).all()

    return {
        "results": [HabitatDropDown.from_orm(habitat) for habitat in habitats]
    }