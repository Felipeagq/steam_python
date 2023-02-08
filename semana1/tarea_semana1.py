personas = []

def agregar_usuario(dataset: list) -> list:
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

while True:
    print("-"*50)
    print(
    """
    Seleccione una acción.
    1. registrar usuario.
    2. actualizar usuario.
    3. eliminar usuario.
    4. visualizar usuarios
    (x) salir
    """
    )
    seleccion = input("selección: ")
    
    if seleccion == "1":
        agregar_usuario(personas)
    
    if seleccion =="3":
        eliminar_usuario(personas)
        
    if seleccion == "4":
        print(personas)
        
    if seleccion == "x":
        break
    print("-"*50)