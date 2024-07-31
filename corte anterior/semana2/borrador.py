import datetime
personas = {"felipe":[
    
    {"libro":"habitos atomicos",
    "fecha":"2023-02-14"},
    
    {"libro":"Club 5 am",
    "fecha":"2023-02-14"},
]}



def agregar_persona(dicccionario:dict)-> dict:
    nombre = input("cual es el nombre de la persona: ")
    libro = input("cual es el libro que presto: ")
    fecha_prestamo = input("Cuando presto el libro: ")
    
    dicccionario_interno = {
        "libro":libro,
        "fecha":fecha_prestamo
    }
    print(dicccionario_interno)
    
    if dicccionario.get(nombre) == None:
        dicccionario[nombre] = [dicccionario_interno]
    else:
        dicccionario[nombre].append(dicccionario_interno)
    # dicccionario[nombre] 
    print(dicccionario)


agregar_persona(personas)