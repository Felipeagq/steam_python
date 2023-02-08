def area_rectangulo(
    a:float,
    b:float
) -> float :
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


print(area_rectangulo(2,3))