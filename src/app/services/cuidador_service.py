# app/services/cuidador_service.py
from sqlalchemy.orm import Session
from app.models.especialidad import Especialidad as EspecialidadModel
from app.models.cuidador import Cuidador
from app.schemas.cuidador import CuidadorCreate, CuidadorSchema, CuidadorUpdate
from fastapi import HTTPException

def create_cuidador(db: Session, cuidador: CuidadorCreate):
    if cuidador.idespecialidad:
        especialidad = db.query(EspecialidadModel).filter(EspecialidadModel.id == cuidador.idespecialidad).first()
        if not especialidad:
            raise HTTPException(status_code=400, detail="Especialidad no encontrada")
    
    nuevo_cuidador = Cuidador(
        nombre=cuidador.nombre,
        fechacontratacion=cuidador.fechacontratacion,
        salario=cuidador.salario,
        idespecialidad=cuidador.idespecialidad,
    )
    db.add(nuevo_cuidador)
    db.commit()
    db.refresh(nuevo_cuidador)
    return nuevo_cuidador

def get_cuidador_by_id(db: Session, cuidador_id: int) -> CuidadorSchema:
    cuidador = db.query(Cuidador).filter(Cuidador.id == cuidador_id).first()
    if not cuidador:
        return None
    return cuidador

def update_cuidador(db: Session, cuidador_id: int, cuidador_update: CuidadorUpdate):
    cuidador = db.query(Cuidador).filter(Cuidador.id == cuidador_id).first()
    if not cuidador:
        raise HTTPException(status_code=404, detail="Cuidador no encontrado")

    if cuidador_update.idespecialidad:
        especialidad = db.query(EspecialidadModel).filter(EspecialidadModel.id == cuidador_update.idespecialidad).first()
        if not especialidad:
            raise HTTPException(status_code=400, detail="Especialidad no encontrada")

    # Actualizar solo los campos enviados
    for key, value in cuidador_update.dict(exclude_unset=True).items():
        setattr(cuidador, key, value)

    db.commit()
    db.refresh(cuidador)
    return cuidador

def delete_cuidador(db: Session, cuidador_id: int) -> bool:
    db_cuidador = db.query(Cuidador).filter(Cuidador.id == cuidador_id).first()
    if not db_cuidador:
        return False
    db.delete(db_cuidador)
    db.commit()
    return True
