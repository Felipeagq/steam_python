# ejercicio 1
# https://www.mclibre.org/consultar/python/ejercicios/ej-funciones-2.html
# Escriba un programa que permita crear dos listas de palabras y que, a continuación,0 
# elimine de la primera lista los nombres de la segunda lista.
# El programa debe preguntar por la cantidad de elementos en cada lista

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)

    numero2 = int(input("Dígame cuántas palabras tiene la lista de palabras a eliminar: "))

    if numero2 < 1:
        print("¡Imposible!")
    else:
        eliminar = []
        for i in range(numero2):
            print("Dígame la palabra", str(i + 1) + ": ", end="")
            palabra = input()
            eliminar += [palabra]
        print("La lista de palabras a eliminar es:", eliminar)

        for i in eliminar:
            for j in range(len(lista)-1, -1, -1):
                if lista[j] == i:
                    del(lista[j])
        print("La lista es ahora:", lista)


# Modifique el programa anterior de manera que el programa solicite dos listas sin repeticiones y escriba el resultado al final

# ejercicio 2 (5)
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.
# {"hola":{
#     "longitud":4
# }}

"hola como estas"
{
    "hola":{
        "longitud":4
    },
    "como":{
        "longitud":4
    },
    "estas":{
        "longitud":5
    }
}

















# Modificación de la tarea # 1
# que ademas del nombre de la persona, pueda guardar un diccionario de los libros que prestó y la fecha
{"felipe":[
    
    {"libro":"habitos atomicos",
    "fecha":"2023-02-14"},
    
    {"libro":"Club 5 am",
    "fecha":"2023-02-15"},
    
    {"libro":"python completo",
    "fecha":"2023-03-05"},
]}

# modificar # 2
# eliminar usuario (con validiación). eliminar libro

# modificar  # 3
# si el libro está prestado o devuelto. validar estado de un libro

{"felipe":[
    
    {"libro":"habitos atomicos",
    "fecha":"2023-02-14",
    "estado":"prestado"},
    
    {"libro":"Club 5 am",
    "fecha":"2023-02-14",
    "estado":"devuelto"},
]}


felipe = [1,2,3]

felipe = []