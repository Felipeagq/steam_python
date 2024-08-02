descuentos = ["DESC1","DESC2"]

cantidad_intentos = int(input("Cuantos intentos tiene el cliente: "))

for i in range(1,cantidad_intentos+1):
    cupon = input("ingresa tu cupon: ")
    if cupon in descuentos:
        print("CUPON ACEPTADO")
        break
    
    print(f"te quedan {cantidad_intentos-i}")

    if (cantidad_intentos-i) == 0:
        print("te quedaste sin intentos")






