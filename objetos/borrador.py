class Triangulo():
    def __init__(self,nombre):
        self.nombre = nombre
        self.a = int(input("introduce el lado a: "))
        self.b = int(input("introduce el lado b: "))
        self.c = int(input("introduce el lado c: "))
        self.lados = [self.a,self.b,self.c]
    
    def lado_mayor(self):
        mayor = max(self.lados)
        print(mayor)
    
    def tipo_triangulo(self):
        conjunto_lados = set(self.lados)
        if len(conjunto_lados) == 3:
            print(f"{self.nombre} es un triangulo escaleno")
        elif len(conjunto_lados) == 2:
            print(f"{self.nombre} es un triangulo isoseles")
        else:
            print(f"{self.nombre} es un triangulo equilatero")



tri = Triangulo("Triangulito")
tri.lado_mayor()
tri.tipo_triangulo()
