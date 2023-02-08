# SEMANA 1

## Instalación de Visual Studio Code.
- Descargar Visual Studio Code. https://code.visualstudio.com/Download
- Instalar dependencias necesarias:
    - Python.
    - indent-rainbow.
    - autoDocstring - Python Docstring Generator.
    - Python Extension Pack.


## 1. Buenas practicas Python
Las buenas practcas en python comprende lo siguiente:
- Declaración de tipo de variables en los parametros.
- Declaración de tipo de dato que retorna.
- Comentarios.
- DocString: documentación de una función.

Como ejemplo sencillo de una función con buenas practicas, tenemos la siguiente función.
````python
# function.py

# Función sin buenas practicas
def area_rectangulo(a,b):
    return a*b


# Función aplicando las buenas practicas
def area_rectangulo(
    a:float,
    b:float
)->float:
    """
        Función para calcular el area de un rectangulo

        Args:
            a (int): Es la altura del rectangulo
            b (int): Es la base del rectangulo

        Returns:
            area (int): Es el area del rectangulo
    """
    area = a*b
    return area
````

## 2. importación de modulos
Nosotros podemos importar diferentes funciones de otros archivos de python, las cuales se le conoce como importación de librerias o modulos.
Existen 3 formas de importar funciones en python 
````python
# main.py

# importando el modulo
import function

# importando la función en especifico
from function import area_rectangulo

# importando todo el modulo
from function import *

````

## 3. name == main
Cuando corremos un archivo de python, este ejecuta todo lo que está en el, pero nosotros podemos definir que se ejecuten ciertas lineas de codigo **SOLO SI ESE ES EL ARCHIVO PRINCIPAL DE LA EJECUCIÓN**, y cuando uno ejecuta un archivo, python le da un nombre temporal como ````__main__```` entonces al decirle ````if __name__ =="__main__"````, le estamos diciendo a python, solo cuando este archivo sea el principal ejecutandose, realiza lo siguente.

Si ponemos eso en efecto, podemos ver el siguiente comportamiento en ````function.py````

````python
def area_rectangulo(
    a:float,
    b:float
):
    """
        Función para calcular el area de un rectangulo

        Args:
            a (int): Es la altura del rectangulo
            b (int): Es la base del rectangulo

        Returns:
            area (int): Es el area del rectangulo
    """
    area = a*b
    return area


# altura = float(input("ingrese altura del rectangulo"))
# base = float(input("ingrese base del rectangulo"))
# print(area_rectangulo(altura,base))

# Lo que viene despues del if, solo se ejecuta si es el archivo principal de ejecución
if __name__ == "__main__":
    altura = float(input("ingrese altura del rectangulo"))
    base = float(input("ingrese base del rectangulo"))
    print(area_rectangulo(altura,base))

````


## 4. Tarea
### Contexto de la tarea
Trabajas en una biblioteca y tienes el trabajo de registrar los usuairos que prestan libros, para eso realizas una script en python donde guardas en un diccionario el nombre del usuario y el nombre del libro de presto, ejemplo ````{"felipe": "habitos atomicos"}````, para que funcione correctamente creas un CRUD (Create, Remove, Update y Delete) con las siguientes funciones ````agregar_usuario, eliminar_usuario, actualizar_usuario, visualiazr_usuario`````
### Requisitos de la Tarea:
- las funciones deben tener buenas practicas con Python.
- El codigo debe cumplir con el principio de Single Responsability, cada archivo de python deben tener un función.
- La tarea debe estar montada en GitHub.
- El archivo principal debe contar con ````__name__=="__main__"````

### Anotaciones.
En el siguiente enlace se cuenta con un **````EJEMPLO INCOMPLETO````** de como deberia ser el programa y el ejemplo está en **````LISTAS````**, los estudiantes deben hacerlo con diccionarios.
