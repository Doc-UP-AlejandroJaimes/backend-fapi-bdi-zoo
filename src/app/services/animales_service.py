# app/services/animales_service.py
from sqlalchemy.orm import Session
from app.models.animales import Animales as AnimalesModel
from app.models.cuidador import Cuidador as CuidadorModel
from app.models.especie import Especie as EspecieModel
from app.models.habitat import Habitat as HabitatModel
from app.schemas.animales import AnimalesCreate, Animales
from fastapi import HTTPException


def create_animal(db: Session, animal: AnimalesCreate):
    # check cuidador
    if animal.idcuidador:
        cuidador = db.query(CuidadorModel).filter(CuidadorModel.id == animal.idcuidador).first()
        if not cuidador:
            raise HTTPException(status_code=400, detail="Cuidador no encontrado")
    # check especie
    if animal.idespecie:
        especie = db.query(EspecieModel).filter(EspecieModel.id == animal.idespecie).first()
        if not especie:
            raise HTTPException(status_code=400, detail="Especie no encontrada")
    # check habitat
    if animal.idhabitat:
        habitat = db.query(HabitatModel).filter(HabitatModel.id == animal.idhabitat).first()
        if not habitat:
            raise HTTPException(status_code=400, detail="Habitat no encontrado")
        
    # create new Animal
    new_animal = AnimalesModel(
        nombre=animal.nombre,
        fechanac=animal.fechanac,
        idcuidador=animal.idcuidador,
        idhabitat=animal.idhabitat,
        idespecie=animal.idespecie,
    )
    db.add(new_animal)
    db.commit()
    db.refresh(new_animal)
    return new_animal

def get_animal_by_id(db: Session, animal_id: int) -> AnimalesModel:
    return db.query(AnimalesModel).filter(AnimalesModel.id == animal_id).first()

def get_animales_paginated(db: Session, page: int, page_size: int):
    """
    Servicio para obtener animales con paginación.
    """
    total = db.query(AnimalesModel).count()  # Total de registros en la tabla
    skip = (page - 1) * page_size  # Cálculo del offset basado en la página actual
    animales = db.query(AnimalesModel).offset(skip).limit(page_size).all()  # Consulta paginada

    return {
        "total": total,
        "page": page,
        "page_size": page_size,
        "results": [Animales.from_orm(animal) for animal in animales]
    }

def delete_animal (db: Session, animal_id: int) -> bool:
    db_animal = db.query(AnimalesModel).filter(AnimalesModel.id == animal_id).first()
    if not db_animal:
        return False
    db.delete(db_animal)
    db.commit()
    return True