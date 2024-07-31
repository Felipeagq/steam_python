# FASTAPI
## Creacion del entorno virtual
1. instalar la libreria del entorno virtual ````pip install virtualenv````
2. creación de entorno virtual ````python -m virtualenv [NOMBRE]````
3. verificamos el python general ````pip freeze```` deben salir varias librerias.
4. Entro a mi entorno virtual (EN WINDOWS desde GIT-BASH) ````source venv/Script/activate```` y sale el nombre de mi entorno virtual en mi linea de comandos.

## Instalar FastAPI
1. instalación de FastAPI ````pip install fastapi uvicorn````
2. creamos un archivo llamado ````entrypoint.py```` y creamos el servidor
```python
from fastapi import FastAPI
app = FastAPI()
```
3. Corremos nuestro servidor ````uvicorn entrypoint:app --reload````

## Metodos HTTP

|metodo|acción DB|uso|
|--|--|--|
|POST| Create| Crear un registro en nuestri Backend o Base de datos|
|GET| Read| acceder, recuprar o leer información|
|PUT| Update | actualizar o editar un registro de nuestro backend o base de datos|
|DELETE| Delete | Eliminar un registro de nuestro backend o base de datos|

## Creación de primera ruta
```python
@app.get("/")
def hello_world_check():
    return {
        "titulo":"Biblioteca",
        "version":"v0.0.0"
    }
```

## Creación de schemas
```python 
from pydantic import BaseModel

class PersonaCreate(BaseModel):
    nombre:str
    edad: int
    ocupacion: str
```