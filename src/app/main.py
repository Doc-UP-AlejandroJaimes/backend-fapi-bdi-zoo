from fastapi import FastAPI
from app.routers import animales, cuidador

app = FastAPI()
version_api = '/v1/'
app.include_router(animales.router, prefix=f"{version_api}animales", tags=["Animales"])
app.include_router(cuidador.router, prefix=f"{version_api}cuidadores", tags=["Cuidadores"])

@app.get("/")
def root():
    return {"message": "¡API funcionando correctamente!"}
