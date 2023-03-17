from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

personas = {
    "1":{
        "nombre":"felipe",
        "edad":23,
        "ocupación":"ingeniero"
    },
    "2":{
        "nombre":"Sharid <3",
        "edad":19,
        "ocupación":"Comunicadora social"
    },
    "3":{
        "nombre":"Samantha",
        "edad":2,
        "ocupación":"Gata"
    }
}


@app.get("/")
def hello_world_check():
    return {
        "titulo":"Biblioteca",
        "version":"v0.0.0"
    }

@app.get("/personas")
def personas_all():
    return personas

class PersonaCreate(BaseModel):
    id:str
    nombre:str
    edad: int
    ocupacion:str
@app.post("/personas")
def personas_add(request:PersonaCreate):
    personas[request.id] = {
        "nombre":request.nombre,
        "edad": request.edad,
        "ocupacion":request.ocupacion
    }
    return personas


@app.put("/personas")
def personas_modify(request:PersonaCreate):
    pass

@app.delete("/personas")
def personas_delete():
    pass