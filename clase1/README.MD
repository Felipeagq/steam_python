# CLASE 1 
- Instalación de Visual Studio Code.
- Repaso de estructura de datos:
    - listas.
    - diccionarios.
    - tuplas.
- Funciones intrínsecas.
- repaso de buenas practicas en funciones:
    - Definir tipado.
    - comentarios.
    - DocString.
    - maximo de 79 caracteres.
- Instalación de GIT.
    - Instalación de git.
    - Creación de cuenta.
    - Primer repositorio.
        - remote add origin
        - add
        - commit.
        - push -u .

## Instalación de Visual Studio Code.
- Descargar Visual Studio Code. https://code.visualstudio.com/Download
- Instalar dependencias necesarias:
    - Python.
    - indent-rainbow.
    - autoDocstring - Python Docstring Generator.
    - Python Extension Pack.

## Repaso de estructura de datos.
- https://docs.python.org/es/3/tutorial/datastructures.html
- https://ricardogeek.com/estructuras-de-datos-en-python/
- https://docs.hektorprofe.net/python/metodos-de-las-colecciones/metodos-de-los-diccionarios/

## Funciones intrínsecas.
- https://docs.python.org/es/3.8/library/functions.html

## Buenas practicas Python
### Tipado en Python.
En Python es posible especificar el tipado de un tipo de datos, este no determina el funcionamiento del script, pero es una ayuda para el programador.
- https://docs.python.org/3/library/typing.html
- https://www.infoworld.com/article/3630372/get-started-with-python-type-hints.html
- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
````python
from typing import List

nombre: str = "Felipe"
edad: int = 23
dinero: float = 8.67 
altura: float= 5.0
base: float = 6.2
````

### Nomenclatura
````python
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name.
````

### Buenas practicas en funciones
Las buenas practicas de las funciones de python incluye, tipado de variables, comentarios y docstring
````python
def area_rectangulo(
    altura:float,
    base:float,
    nombre:str
) -> str:
    response = f" {nombre} tiene un rectangulo de area {base*altura}"
    return response
````