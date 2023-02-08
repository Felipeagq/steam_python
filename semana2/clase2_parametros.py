class ClasePractica():
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
p1 = ClasePractica("felipe",23)
print(p1.edad, p1.nombre)
print(p1)