def suma_1(a,b):
    return a*b

def suma_2(
    a:int,
    b:int,
) -> str:
    """_summary_

    Args:
        a (int): Es la altura del rec
        b (int): es la base del rectangulo 

    Returns:
        str: multiplicación
    """
    return f"tiene area: {a*b}"

print(suma_2("a",4))

print(suma_2("a","b"))

print(suma_2("a",1.3))
