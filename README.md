# BACKEND-FAPI-BDI-ZOO
# 🚀 Proyecto: Backend para Zoológico

**Desarrollador**: Alejandro Jaimes  
**Directorio Fuente**: `/src/GitHub - Projects/Doc-UP-AlejandroJaimes/BACKEND-FAPI-BDI-ZOO` 📂  
**Creado**: 23-Octubre-2024 🗓️  
**Última Actualización**: 04-Diciembre-2024 ✨  

## Descripción
Este proyecto es un backend desarrollado en **FastAPI** para la gestión de datos en un zoológico. Utiliza **PostgreSQL** como base de datos y está diseñado con una arquitectura modular que facilita la escalabilidad y el mantenimiento.

Las contribuciones y los comentarios siempre son bienvenidos. ¡Explora y descubre la magia en el directorio `/src`! ⚡

---

## Estructura del Proyecto

### [docs/](./docs/)
**Propósito**: Centraliza toda la documentación relevante del proyecto.

**Contenido**:
- `README.md`: Documentación general del proyecto.
- `API_Documentation.md`: Detalles de los endpoints desarrollados con FastAPI.
- `Database_Diagram.png`: Diagrama de la base de datos utilizada.

---

### [src/app/](./src/app/)
**Propósito**: Contiene el código fuente principal del proyecto.

**Subcarpetas**:
- **[database/](./src/app/database/):**  
  Configuración de la conexión a PostgreSQL.  
  - `database.py`: Archivo que gestiona la conexión con la base de datos.

- **[models/](./src/app/models/):**  
  Definición de los modelos SQLAlchemy.  
  - `cuidador.py`: Modelo para la entidad "Cuidador".  
  - `especialidad.py`: Modelo para la entidad "Especialidad".

- **[routers/](./src/app/routers/):**  
  Contiene los endpoints para las APIs.  
  - `cuidador.py`: API para gestionar cuidadores.  
  - `especialidad.py`: API para gestionar especialidades.

- **[schemas/](./src/app/schemas/):**  
  Esquemas de Pydantic para validación y serialización de datos.  
  - `cuidador.py`: Esquema para la entidad "Cuidador".  
  - `especialidad.py`: Esquema para la entidad "Especialidad".

- **[services/](./src/app/services/):**  
  Lógica de negocio y acceso a la base de datos.  
  - `cuidador_service.py`: Servicios relacionados con cuidadores.  
  - `especialidad_service.py`: Servicios relacionados con especialidades.

**Archivo Principal**:
- `main.py`: Punto de entrada de la aplicación.
---

### [data/](./data/)
**Propósito**: Carpeta para almacenar datos relacionados con la base de datos.

**Subcarpetas**:
- **[backups/](./data/backups/):** Respaldo de la base de datos.  
- **[fixtures/](./data/fixtures/):** Datos de prueba para poblar la base de datos.

---

### [scripts/](./scripts/)
**Propósito**: Scripts útiles para la automatización y configuración.

**Subcarpetas**:
- **[database/](./scripts/database/):**  
  Scripts SQL para inicializar o gestionar la base de datos.  
  - `init_db.sql`: Inicialización de la base de datos.  
  - `reset_db.sql`: Restablecimiento de la base de datos.

---

## Requisitos

- **Python 3.9+**
- **PostgreSQL**

---

## Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/usuario/BACKEND-FAPI-BDI-ZOO.git
cd BACKEND-FAPI-BDI-ZOO

## Instalación

Sigue los pasos a continuación para configurar y ejecutar el proyecto:

### 1. Clonar el Repositorio

```bash
git clone https://github.com/usuario/BACKEND-FAPI-BDI-ZOO.git
cd BACKEND-FAPI-BDI-ZOO
```

### 2. Crear un Entorno Virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar las Dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar las Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto con la siguiente configuración (ajusta los valores según tu entorno):

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=zoologico
DB_USER=user
DB_PASSWORD=password
APP_ENV=development
SECRET_KEY=tu_clave_secreta
```

### 5. Inicializar la Base de Datos

Asegúrate de que tu base de datos exista, y esté corriendo en el puerto predispuesto para correr, `postgresql` por defecto corre en el puerto 5432