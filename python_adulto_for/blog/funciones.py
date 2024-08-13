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