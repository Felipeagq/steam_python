# ejercicio 2 (5)
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
#

def palabras2 (
    x:str    
) -> dict:
    x = x.split(" ")
    print(x)
    diccionario = {}
    
    
    for palabra in x:
        longitud = len(palabra)
        diccionario[palabra] = {
            "longitud": longitud
        }
    print(diccionario)


def palabras (
    x:str    
) -> dict:
    x = x.split(" ")
    print(x)
    diccionario = {}
    
    for palabra in x:
        diccionario_interno = {"longitud":len(palabra)}
        diccionario[palabra] = diccionario_interno
    print(diccionario)
    
    
palabras("Hola buenas noches")

