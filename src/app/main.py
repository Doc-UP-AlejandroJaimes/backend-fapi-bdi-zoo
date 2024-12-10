from fastapi import FastAPI
from app.routers import animales, cuidador
from mangum import Mangum

app = FastAPI()

@app.get("/")
def root():
    return {"message": "¡API funcionando correctamente!"}

handler = Mangum(app)
version_api = '/v1/'
app.include_router(animales.router, prefix=f"{version_api}animales", tags=["Animales"])
app.include_router(cuidador.router, prefix=f"{version_api}cuidadores", tags=["Cuidadores"])
