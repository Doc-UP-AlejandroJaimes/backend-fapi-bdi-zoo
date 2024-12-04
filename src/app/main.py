from fastapi import FastAPI
from app.routers import animales, cuidador

app = FastAPI()

app.include_router(animales.router, prefix="/animales", tags=["Animales"])
app.include_router(cuidador.router, prefix="/cuidadores", tags=["Cuidadores"])

@app.get("/")
def root():
    return {"message": "¡API funcionando correctamente!"}
