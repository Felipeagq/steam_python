# gestor de  blog 
# 1. login
# 2. hacer un post (titulo, subtitulo, descripción) : autenticarme
# 3. listar todos los post de una persona
# 4. debo poder eliminar el post de una persona : autenticarme
# 5. debo poder salir del programa.

# funciones, diccionario, lista, if 

usuarios = [
    {'user': 'felipe', 'pass': 'felipe123'}, 
    {'user': 'cyan', 'pass': 'cyan123'}
]

publicaciones = [{'titulo': 'hola', 'descripcion': 'hay dios mio', 'autor': 'felipe'},
            {'titulo': 'aja', 'descripcion': 'carambaaaa', 'autor': 'felipe'}]  

def create_post(titulo,descripcion,autor):
    create_post = {
        "titulo":titulo,
        "descripcion":descripcion,
        "autor": autor
    }
    publicaciones.append(create_post)

def create_user(user,psd):
    usuario = {
        "user":user,
        "pass":psd
    }
    usuarios.append(usuario)

def eliminar_post(titulo):
    for i in publicaciones:
        if i.get("titulo") == titulo:
            publicaciones.remove(i)
            
    
    
def listar_post(autor):
    lista_publicaciones = []
    for i in publicaciones:
        if i.get("autor") == autor:
            lista_publicaciones.append(i)
    print(lista_publicaciones)
            
    
def login(user,psd):
    usuario_validado = False
    password_validado = False
    for usuario in usuarios:
        for key,value in usuario.items():
            if key == "user" and value == user:
                usuario_validado = True
            if key == "pass" and value == psd:
                password_validado = True
    if usuario_validado == True and password_validado == True:
        return True
    return False

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