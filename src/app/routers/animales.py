from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.animales_service import  get_animal_by_id
from app.schemas.animales import Animales

router = APIRouter()


@router.get("/{animal_id}", response_model=Animales)
def get_animal_endpoint(animal_id: int, db: Session = Depends(get_db)):
    print(Animales)
    animal = get_animal_by_id(db, animal_id)
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal