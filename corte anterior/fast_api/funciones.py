from fastapi import FastAPI
from schemas import PersonaBiblioteca, PersonaModify


app = FastAPI()

biblioteca = []

# registramos una función en mi app en ruta (endpoint)
# "/" ruta raiz
# Solo podemos tener una función por verbo en una ruta
@app.get("/")
def hello_world_check():
    return  {
        "titulo":"bilioteca STEAM",
        "version":"v0.0.1"
    }


@app.get("/personas")
def personas_all():
    """Me regresa todas las personas 
    registrada en mi biblioteca

    Returns:
        biblioteca [list]
    """
    return biblioteca

@app.get("/personas/{id}")
def personas_one(id:str):
    """Me retorno la persona con un id

    Args:
        id (str): El id de la persona

    Returns:
        bilioteca[id] [dict]: es la información basica
                                de la persona
    """
    for i in biblioteca:
        if i.id == id:
            print(i.id)
            return i
    return {"error":"Persona no encontrada"}


@app.post("/personas")
def personas_add(request:PersonaBiblioteca):
    biblioteca.append(request)
    return request



@app.put("/persona")
def personas_modify(request:PersonaModify):
    for i in biblioteca:
        print(i)
        if i.id == request.id:
            i.nombre = request.nombre
            i.edad = request.edad
            return i
    return {"error":"Persona no encontrada"}


@app.delete("/personas/{id}")
def personas_delete(id:str):
    for i in biblioteca:
        if i.id == id:
            print(i.id)
            return i
    return {"error":"Persona no encontrada"}