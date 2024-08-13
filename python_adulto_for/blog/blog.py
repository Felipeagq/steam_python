# gestor de  blog 
# 1. login
# 2. hacer un post (titulo, subtitulo, descripción) : autenticarme
# 3. listar todos los post de una persona
# 4. debo poder eliminar el post de una persona : autenticarme
# 5. debo poder salir del programa.

# funciones, diccionario, lista, if 


from funciones import *



while True:
    accion =input("""
          Que desea hacer:
          1. salir del programa
          2. agregar usuario
          3. eliminar un post
          4. agrega un post
          5. lista todos tus post
          6. listar todos los post
          ------------------------
          """)
    
    if accion == "1":
        break
    elif accion == "2":
        user = input("ingresa usuairo: ")
        psd = input("ingresa constraseña: ")
        create_user(user,psd)
        print("-"*50)
    
    elif accion == "4":
        user = input("ingresa usuairo: ")
        psd = input("ingresa constraseña: ")
        usuario = login(user,psd)
        print("puedes agregar un post: ")
        while usuario:
            titulo = input("agrega un titulo: ")
            descripcion = input("agrega un descripción: ")
            create_post(titulo,descripcion,user)
            print(publicaciones)
            salir = input("¿deseas salir ? si/no:  ")
            if salir == "si":
                break
            
        else:
            print("Hey tu usuario no existe")
            
    elif accion == "5":
        user = input("ingresa usuairo: ")
        psd = input("ingresa constraseña: ")
        usuario = login(user,psd)
        if usuario:
            listar_post(user)
    
    elif accion == "3":
        user = input("ingresa usuairo: ")
        psd = input("ingresa constraseña: ")
        usuario = login(user,psd)
        if usuario:
            listar_post(user)
            A = input("cual es el titulo: ")
            eliminar_post(A) 
            listar_post(user)
        
    
        


print(usuarios)