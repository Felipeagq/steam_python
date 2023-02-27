# # numero = 3
# # flotante = 2.4
# # cadena = "felipe"

# # print(type(numero))
# # print(type(flotante))
# # print(type(cadena))

# class Personas():
#     sentidos = ["bista","holfato","takto","guzto","hoido"]
    
#     def __init__(self,nombre,edad, apellido, profesion) -> None:
#         self.nombre = nombre
#         self.edad = edad
#         self.apellido = apellido
#         self.profesion = profesion
        
#     def __str__(self) -> str:
#         return f"{self.nombre} tiene {self.edad} años"

#     def area_rectangulo(self,
#         altura:float,
#         base:float,
#         nombre:str
#     ) -> str:
#         area = base * altura
#         response = f"{nombre} tiene un rectangulo de area {area}"
#         print(response)
        
#     def saludo(self):
#         print(f"hola {self.nombre} {self.apellido}, ¿como estas?")

# p1 = Personas("gabriela","24","giraldo","estudiante")
# p2 = Personas("felipe","23","gonzalez","batman")

# print(p1.nombre)
# print(p2.nombre)

# print(p1.area_rectangulo(2,3,"felipe"))
# p1.saludo()


class Personas():
    # libros = {}
    
    def __init__(self,nombre,apellido,edad,colegio):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        self.colegio = colegio
        self.libros = {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "edad":self.edad,
            "colegio":self.colegio,
            "libros":{}
        }
    def agregar(self,nom_libro,fecha):
        self.libros["libros"].update({nom_libro:fecha})


p1 = Personas("felipe","gonzalez","23","BIS")
p2 = Personas("gabriela","gonzalez","23","BIS")

p2.agregar("python","24/02/2023")
p2.agregar("java","12/02/2023")

p1.agregar("docker","24/02/2023")
p1.agregar("aws","12/02/2023")

print(p2.libros)
print("\n")
print(p1.libros)

