class ClasePractica():
    def __init__(self,
                nombre:str,
                edad:int) -> None:
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self) -> str:
        return f"{self.nombre} tiene {self.edad} años"
        
p1 = ClasePractica("felipe",23)
print(p1.edad, p1.nombre)
print(p1)