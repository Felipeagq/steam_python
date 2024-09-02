Aquí tienes algunos ejercicios en Python para practicar el uso de `try` y `except`:

### Ejercicio 1: División segura
Escribe un programa que pida al usuario dos números e intente dividirlos. Usa un bloque `try` para manejar posibles errores como la división por cero y la introducción de datos no numéricos.

**Código ejemplo:**

```python
try:
    numerador = float(input("Introduce el numerador: "))
    denominador = float(input("Introduce el denominador: "))
    resultado = numerador / denominador
    print(f"El resultado es: {resultado}")
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
except ValueError:
    print("Error: Por favor introduce solo números.")
```

### Ejercicio 2: Manejo de archivos
Escribe un programa que abra un archivo de texto y cuente cuántas líneas contiene. Usa `try` y `except` para manejar la situación en la que el archivo no existe.

**Código ejemplo:**

```python
try:
    with open('archivo.txt', 'r') as file:
        lineas = file.readlines()
        print(f"El archivo contiene {len(lineas)} líneas.")
except FileNotFoundError:
    print("Error: El archivo no se encontró.")
```

### Ejercicio 3: Suma de elementos de una lista
Crea un programa que sume los elementos de una lista que contenga números y otros tipos de datos. Utiliza `try` y `except` para manejar errores cuando el programa intente sumar elementos que no sean números.

**Código ejemplo:**

```python
elementos = [1, 2, 'a', 3, 4, 'b']
suma = 0

for elemento in elementos:
    try:
        suma += elemento
    except:
        print(f"Error: No se puede sumar {elemento} porque no es un número.")

print(f"La suma de los números en la lista es: {suma}")
```

### Ejercicio 4: Entrada válida de edad
Escribe un programa que pida al usuario que introduzca su edad. Usa `try` y `except` para asegurarte de que el usuario introduce un número positivo.

**Código ejemplo:**

```python
try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")
    print(f"Tu edad es: {edad}")
except:
    print(f"Error: {ve}")
```

### Ejercicio 5: Entrada de múltiples valores
Pide al usuario que introduzca varios números separados por comas. Usa `try` y `except` para manejar errores si el usuario no introduce los números correctamente.

**Código ejemplo:**

```python
try:
    entrada = input("Introduce varios números separados por comas: ")
    numeros = [int(n) for n in entrada.split(',')]
    print(f"Has introducido los números: {numeros}")
except ValueError:
    print("Error: Asegúrate de introducir solo números separados por comas.")
```

Estos ejercicios te ayudarán a practicar el manejo de excepciones en Python y a aprender a manejar errores de manera efectiva en tu código.
