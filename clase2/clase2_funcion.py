class ClasePractica():
    def __init__(self,
                altura:int,
                base:int,
                nombre:str = "Felipe",
                edad:int = 23,
                ) -> None:
        self.nombre = nombre
        self.edad = edad
        self.base = base
        self.altura = altura
    
    def __str__(self) -> str:
        return f"{self.nombre} tiene {self.edad} años"
    
    def area_rectangulo( self,
        # altura:float,
        # base:float,
        # nombre:str
    ) -> str:
        response = f" {self.nombre} tiene un rectangulo de area {self.base*self.altura}"
        print(response)
        
p1 = ClasePractica(5,7)
print(p1.edad, p1.nombre)
p1.area_rectangulo()
print(p1)

