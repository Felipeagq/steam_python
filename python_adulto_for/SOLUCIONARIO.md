# SOLUCIONARIO FOR

````PY
# Ejercicio 1
valid_codes = ['DESC10', 'SAVE20', 'PROMO30']
attempts = 5

for attempt in range(attempts):
    code = input("Ingrese su código de descuento: ").strip().upper()
    
    if code in valid_codes:
        print("¡Código válido! Descuento aplicado.")
        break
    else:
        print("Código inválido. Intente nuevamente.")
        if attempt == attempts - 1:
            print("Se acabaron los intentos. No se pudo aplicar el descuento.")
````

```` py
# Ejercicio 2
forbidden_words = ['spam', 'advertisements', 'fake']
messages = []

while True:
    message = input("Ingrese su mensaje (o 'salir' para terminar): ").strip()
    
    if message.lower() == 'salir':
        break
    
    contains_forbidden = False
    for word in forbidden_words:
        if word in message.lower():
            contains_forbidden = True
            print("Mensaje contiene una palabra prohibida y será ignorado.")
            break
    
    if contains_forbidden:
        continue
    
    messages.append(message)
    print("Mensaje agregado.")
````

````py
grades = []

while True:
    entry = input("Ingrese una nota (o 'fin' para terminar): ").strip()
    
    if entry.lower() == 'fin':
        break
    

    grade = float(entry)
    if 0 <= grade <= 100:
        grades.append(grade)
    else:
        print("Nota fuera de rango. Ingrese una nota entre 0 y 100.")

        
if grades:
    average = sum(grades) / len(grades)
    print(f"El promedio de las notas es: ", average)
else:
    print("No se ingresaron notas válidas.")
````