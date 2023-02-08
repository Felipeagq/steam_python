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

if __name__ == "__main__":
    altura = float(input("ingrese altura del rectangulo"))
    base = float(input("ingrese base del rectangulo"))
    print(area_rectangulo(altura,base))