# CLICOS EN PYTHON 

## Ciclos FOR

El ciclo `for` en Python se utiliza para iterar sobre una secuencia (como una lista, una tupla, un diccionario, un conjunto o una cadena de caracteres). La sintaxis básica es:

```python
for elemento in secuencia:
    # Bloque de código a ejecutar por cada elemento
```

**Ejemplo**:

```python
# Iterando sobre una lista
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

En este ejemplo, `numero` toma el valor de cada elemento en la lista `numeros` durante cada iteración del bucle, y se imprime cada valor.

### Uso de `break`

La instrucción `break` se utiliza para terminar el bucle de forma prematura, es decir, cuando se cumple una condición específica. El control del programa se pasa a la siguiente declaración después del bucle.

**Ejemplo**:

```python
# Iterando sobre una lista con break
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 3:
        break
    print(numero)
```

Salida:
```
1
2
```

En este ejemplo, el bucle se detiene cuando `numero` es igual a 3, por lo que no se imprimen los números 3, 4 y 5.

### Uso de `continue`

La instrucción `continue` se utiliza para omitir el resto del código dentro del bucle para la iteración actual y pasar a la siguiente iteración del bucle.

**Ejemplo**:

```python
# Iterando sobre una lista con continue
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 3:
        continue
    print(numero)
```

Salida:
```
1
2
4
5
```

En este ejemplo, cuando `numero` es igual a 3, la instrucción `continue` hace que se omita la impresión de 3 y se pase directamente a la siguiente iteración del bucle.

### Ejemplo Completo

Aquí hay un ejemplo que combina `for`, `break` y `continue`:

```python
# Iterando sobre una lista con break y continue
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for numero in numeros:
    if numero == 7:
        break  # Detener el bucle cuando el número es 7
    if numero % 2 == 0:
        continue  # Saltar la impresión de los números pares
    print(numero)
```

Salida:
```
1
3
5
```

En este ejemplo:
- El bucle se detiene cuando `numero` es igual a 7 debido a la instrucción `break`.
- La instrucción `continue` hace que los números pares (2, 4, 6) no se impriman.

Este es el uso básico y la sintaxis del ciclo `for` junto con las instrucciones `break` y `continue` en Python.

## Ciclos While


El ciclo `while` en Python se utiliza para repetir un bloque de código mientras una condición sea verdadera. La sintaxis básica es:

```python
while condición:
    # Bloque de código a ejecutar mientras la condición sea verdadera
```

**Ejemplo**:

```python
# Iterando con while
contador = 0

while contador < 5:
    print(contador)
    contador += 1
```

En este ejemplo, el bloque de código dentro del `while` se ejecuta mientras la variable `contador` sea menor que 5. En cada iteración, `contador` se incrementa en 1.

### Uso de `break`

La instrucción `break` se utiliza para terminar el bucle de forma prematura, es decir, cuando se cumple una condición específica. El control del programa se pasa a la siguiente declaración después del bucle.

**Ejemplo**:

```python
# Iterando con while y break
contador = 0

while contador < 10:
    if contador == 5:
        break
    print(contador)
    contador += 1
```

Salida:
```
0
1
2
3
4
```

En este ejemplo, el bucle se detiene cuando `contador` es igual a 5 debido a la instrucción `break`.

### Uso de `continue`

La instrucción `continue` se utiliza para omitir el resto del código dentro del bucle para la iteración actual y pasar a la siguiente iteración del bucle.

**Ejemplo**:

```python
# Iterando con while y continue
contador = 0

while contador < 10:
    contador += 1
    if contador % 2 == 0:
        continue
    print(contador)
```

Salida:
```
1
3
5
7
9
```

En este ejemplo, cuando `contador` es un número par, la instrucción `continue` hace que se omita la impresión y se pase directamente a la siguiente iteración del bucle.

### Ejemplo Completo

Aquí hay un ejemplo que combina `while`, `break` y `continue`:

```python
# Iterando con while, break y continue
contador = 0

while contador < 10:
    contador += 1
    if contador == 7:
        break  # Detener el bucle cuando el contador es 7
    if contador % 2 == 0:
        continue  # Saltar la impresión de los números pares
    print(contador)
```

Salida:
```
1
3
5
```

En este ejemplo:
- El bucle se detiene cuando `contador` es igual a 7 debido a la instrucción `break`.
- La instrucción `continue` hace que los números pares (2, 4, 6) no se impriman.



---
---
---
## Ejercicios de practica

### Ejercicio de practica 1
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

### Ejercicios de practica 2
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.



## Ejercicio 1  Validación de Códigos de Descuento
Descripción: Imagina que trabajas para una tienda en línea que ofrece varios códigos de descuento a sus clientes. Quieres crear un programa en Python que permita a los usuarios ingresar un código de descuento y verificar si es válido. Los códigos válidos están almacenados en una lista predefinida. El programa debe permitir al usuario hasta cinco intentos para ingresar un código correcto. Si el usuario ingresa un código válido, el programa debe imprimir un mensaje de éxito y terminar. Si el usuario agota los cinco intentos sin ingresar un código válido, el programa debe imprimir un mensaje indicando que se han acabado los intentos.

## Ejercicios 2 Filtrado de Mensajes en un Chat
Descripción: Estás desarrollando un sistema de chat que necesita filtrar mensajes que contienen ciertas palabras prohibidas. Los usuarios pueden ingresar mensajes, pero si un mensaje contiene una palabra prohibida, debe ser ignorado. El sistema debe permitir a los usuarios continuar ingresando mensajes hasta que escriban 'salir' para finalizar.

## Ejercicio 3 Cálculo de Promedio de Notas
Descripción: Un profesor desea calcular el promedio de las notas de sus estudiantes. Los estudiantes ingresan sus notas una a una. Si se ingresa una nota fuera del rango de 0 a 100, el programa debe ignorar esa entrada y solicitar una nueva nota. El programa debe detenerse cuando se ingrese la palabra 'fin' y luego calcular el promedio de las notas válidas ingresadas.

# TAREAS 
Investigar.
- Listas y sus metodos.
- Diccionarios y sus metodos.
- string y sus metodos.
- Que son los modulos y como crearlos.
