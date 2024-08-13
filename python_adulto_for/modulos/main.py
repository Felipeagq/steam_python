# from funciones import suma_dos,resta_dos,multiplicacion_dos

from operaciones.funciones import (
    suma_dos as suma, 
    resta_dos,
    multiplicacion_dos
)

# from funciones import * # todo

# import operaciones.funciones
# from operaciones import funciones
# from operaciones.funciones import #

primero = int(input("ingresa el primer numero: "))
segundo = int(input("ingresa el segundo numero: "))

suma = suma(primero,segundo)
print(suma)

resta = resta_dos(primero,segundo)
print(resta)

multiplicacion = multiplicacion_dos(primero,segundo)
print(multiplicacion)