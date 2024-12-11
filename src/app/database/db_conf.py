from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    app_env: str = "development"  # Valor predeterminado si no está en el entorno
    secret_key: str

    class Config:
        # Elimina la referencia al archivo .env
        env_file = ".env"  # Desactiva el archivo .env para AWS Lambda
        #env_file = None  # Desactiva el archivo .env para AWS Lambda

# Instancia global de configuración
settings = Settings()