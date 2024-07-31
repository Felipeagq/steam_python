# class Triangulo():
#     def __init__(self,nombre):
#         self.nombre = nombre
#         self.a = int(input("introduce el lado a: "))
#         self.b = int(input("introduce el lado b: "))
#         self.c = int(input("introduce el lado c: "))
#         self.lados = [self.a,self.b,self.c]
    
#     def lado_mayor(self):
#         mayor = max(self.lados)
#         print(mayor)
    
#     def tipo_triangulo(self):
#         conjunto_lados = set(self.lados)
#         if len(conjunto_lados) == 3:
#             print(f"{self.nombre} es un triangulo escaleno")
#         elif len(conjunto_lados) == 2:
#             print(f"{self.nombre} es un triangulo isoseles")
#         else:
#             print(f"{self.nombre} es un triangulo equilatero")

# tri = Triangulo("Triangulito")
# tri.lado_mayor()
# tri.tipo_triangulo()







# class Cuenta():
#     def __init__(self,titular,cantidad):
#         self.titular = titular
#         self.cantidad = cantidad
        
#     def mostrar(self):
#         print(self.cantidad)
    
#     def ingresar(self,c):
#         self.cantidad = self.cantidad + c
#         print(f"tu cantidad ahroa es {self.cantidad}")

#     def retirar(self,c):
#         self.cantidad = self.cantidad - c
#         print(f"tu cantidad ahroa es {self.cantidad}")

# p1 = Cuenta("felipe",100)
# p1.ingresar(27)
# p1.retirar(39)




class SerVivo():
    sentidos_listado = ["olfato","vista","tacto"]
    
    def __init__(self,nombre):
        self.nombre = nombre
    
    def sonido(self):
        print(f"{self.nombre} está haciendo un sonido")
        
    def movimiento(self):
        print(f"{self.nombre} se está moviendo")

class Humano(SerVivo):
    
    def movimiento(self):
        print(f"{self.nombre} está caminando")

class Gato(SerVivo):
    def movimiento(self):
        print(f"{self.nombre} está galopando")
    
    def __str__(self)->None:
        return f"{self.nombre}"

servivo = SerVivo("Guakua")
servivo.movimiento()
servivo.sonido()
print(servivo.sentidos_listado)
print("-"*20)
homosapien = Humano("Rodolfo")
homosapien.movimiento()
homosapien.sonido()
print(homosapien.sentidos_listado)
print("-"*20)
michu = Gato("Samantha")
michu.movimiento()
michu.sonido()
print(michu.sentidos_listado)
print("-"*20)
print(michu)