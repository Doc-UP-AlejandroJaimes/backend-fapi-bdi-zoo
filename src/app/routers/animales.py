from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.animales_service import  get_animal_by_id, create_animal, get_animales_paginated, delete_animal
from app.schemas.animales import AnimalesGetEndpoint, AnimalesCreate

router = APIRouter()

@router.get("/", response_model=dict)
def get_animales_endpoint(
    page: int = Query(1, ge=1),  # Página actual (1-indexed)
    page_size: int = Query(10, le=100),  # Tamaño de página
    db: Session = Depends(get_db),
):
    """
    Endpoint para traer animales con paginación.
    """
    result = get_animales_paginated(db=db, page=page, page_size=page_size)
    return result

@router.post("/", response_model=AnimalesCreate)
def create_animal_endpoint(animal: AnimalesCreate, db: Session = Depends(get_db)):
    return create_animal(db, animal)

@router.get("/{animal_id}", response_model=AnimalesGetEndpoint)
def get_animal_endpoint(animal_id: int, db: Session = Depends(get_db)):
    animal = get_animal_by_id(db, animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return animal
@router.delete("/{animal_id}")
def delete_animal_endpoint(animal_id: int, db: Session = Depends(get_db)):
    if not delete_animal(db, animal_id):
        raise HTTPException(status_code=404, detail="Animal no encontrado")
    return {"detail": "Animal eliminado con éxito"}
