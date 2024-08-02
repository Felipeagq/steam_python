# gestor de  blog 
# 1. login
# 2. hacer un post (titulo, subtitulo, descripción) : autenticarme
# 3. listar todos los post de una persona
# 4. debo poder eliminar el post de una persona : autenticarme
# 5. debo poder salir del programa.

# funciones, diccionario, lista, if 

usuarios = []

def login(user,psd):
    usuario = {
        "user":user,
        "pass":psd
    }
    usuarios.append(usuario)
    
while True:
    accion =input("""
          Que desea hacer:
          1. salir del programa
          2. agregar usuario
          3. eliminar un post
          4. agrega un post
          5. lista todos tus post
          ------------------------
          """)
    accion = int(accion)
    if accion == 1:
        break
    elif accion == 2:
        user = input("ingresa usuairo: ")
        psd = input("ingresa constraseña: ")
        login(user,psd)
        print("-"*50)


print(usuarios)