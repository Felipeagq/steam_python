def agregar_usuario(dataset: list) -> list:
    """_summary_

    Args:
        dataset (list): _description_

    Returns:
        list: _description_
    """
    dato = input("ingrese un dato :")
    dataset.append(dato)

def eliminar_usuario(dataset: list) -> list:
    dato = input("ingrese un dato :")
    dataset.remove(dato)

def actualizar_usuario(dataset: list) -> list:
    dato1 = input("ingrese viejo dato actualizar:")
    dato2 = input("ingrese nuevo dato actualizar:")
    dataset.remove(dato1)
    dataset.append(dato2)

def visualiazr_usuario(dataset: list) -> list:
    dato = input("ingrese un dato :")
    dataset.append(dato)