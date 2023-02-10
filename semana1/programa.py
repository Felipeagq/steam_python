from funciones_tarea import *

def programa(personas):
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