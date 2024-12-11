from fastapi import FastAPI
from app.routers import animales, especies, habitats, cuidadores
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ljr9in3d88.execute-api.us-east-1.amazonaws.com","http://localhost:5173"],  # Permite todas las solicitudes de cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)

version_api = '/v1/'
app.include_router(animales.router, prefix=f"{version_api}animales", tags=["Animales"])
app.include_router(cuidadores.router, prefix=f"{version_api}cuidadores", tags=["Cuidadores"])
app.include_router(especies.router, prefix=f"{version_api}especies", tags=["Especies"])
app.include_router(habitats.router, prefix=f"{version_api}habitats", tags=["Habitats"])

@app.get("/")
def root():
    return {"message": "¡API funcionando correctamente!"}

handler = Mangum(app)

