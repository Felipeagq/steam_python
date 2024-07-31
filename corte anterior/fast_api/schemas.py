from pydantic import BaseModel

class PersonaBiblioteca(BaseModel):
    id:str
    nombre:str
    edad:int
    libros:dict
    
class PersonaModify(BaseModel):
    id:str
nombre:str
edad:int