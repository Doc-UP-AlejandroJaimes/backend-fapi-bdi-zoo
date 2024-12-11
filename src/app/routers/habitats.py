from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.habitat_service import get_habitats

router = APIRouter()

@router.get("/", response_model=dict)
def get_habitats_endpoint(
    db: Session = Depends(get_db),
):
    """
    Endpoint para traer habitats.
    """
    result = get_habitats(db=db,)
    return result
