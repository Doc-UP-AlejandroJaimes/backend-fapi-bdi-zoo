# app/services/animales_service.py
from sqlalchemy.orm import Session
from app.models.animales import Animales as AnimalesModel


def get_animal_by_id(db: Session, animal_id: int) -> AnimalesModel:
    return db.query(AnimalesModel).filter(AnimalesModel.id == animal_id).first()
