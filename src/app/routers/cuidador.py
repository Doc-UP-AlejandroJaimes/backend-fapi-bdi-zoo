from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.cuidador_service import (
    create_cuidador,
    get_cuidador_by_id,
    update_cuidador,
    delete_cuidador,
)
from app.schemas.cuidador import CuidadorSchema, CuidadorCreate, CuidadorUpdate

router = APIRouter()


@router.post("/", response_model=CuidadorSchema)
def create_cuidador_endpoint(cuidador: CuidadorCreate, db: Session = Depends(get_db)):
    return create_cuidador(db, cuidador)

@router.get("/{cuidador_id}", response_model=CuidadorSchema)
def get_cuidador_endpoint(cuidador_id: int, db: Session = Depends(get_db)):
    cuidador = get_cuidador_by_id(db, cuidador_id)
    if not cuidador:
        raise HTTPException(status_code=404, detail="Cuidador not found")
    return cuidador

@router.put("/{cuidador_id}", response_model=CuidadorSchema)
def update_cuidador_endpoint(cuidador_id: int, cuidador_update: CuidadorUpdate, db: Session = Depends(get_db)):
    print("Cuerpo recibido (crudo):", cuidador_update.dict(exclude_unset=True, by_alias=True))
    print("Cuerpo recibido (sin alias):", cuidador_update.dict(exclude_unset=True, by_alias=False))
    return update_cuidador(db, cuidador_id, cuidador_update)

@router.delete("/{cuidador_id}")
def delete_cuidador_endpoint(cuidador_id: int, db: Session = Depends(get_db)):
    if not delete_cuidador(db, cuidador_id):
        raise HTTPException(status_code=404, detail="Cuidador not found")
    return {"detail": "Cuidador deleted successfully"}
