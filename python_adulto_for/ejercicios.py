# descuentos = ["DESC1","DESC2"]
# cantidad_intentos = int(input("Cuantos intentos tiene el cliente: "))
# for i in range(1,cantidad_intentos+1):
#     cupon = input("ingresa tu cupon: ")
#     if cupon in descuentos:
#         print("CUPON ACEPTADO")
#         break
#     print(f"te quedan {cantidad_intentos-i}")
#     if (cantidad_intentos-i) == 0:
#         print("te quedaste sin intentos")


# palabras_prohibidas = ["bobo","tonto","pendejo"]
# while True:
#     mensaje = input("mensaje: ")
#     if mensaje == "salir":
#         break
#     flag = 0 
#     for palabra in palabras_prohibidas:
#         if  palabra in mensaje:
#             flag = 1
#             print("Su mensaje fue Baneado por mal hablado")
#     if flag:
#         continue
#     print(mensaje)

notas = []
while True:
    nota = input("ingresa tu nota:  ")
    if nota =="fin":
        break
    nota = int(nota)
    if nota > 100 or nota < 0:
        print("ingresa tu nota otra vez, tu nota debe estar entre 0-100")
        continue
    notas.append(nota)

promedio = (sum(notas))/len(notas)
print(f"el promedio del salon es {promedio:.1f}")





