# # # numero = 3
# # # flotante = 2.4
# # # cadena = "felipe"

# # # print(type(numero))
# # # print(type(flotante))
# # # print(type(cadena))

# # class Personas():
# #     sentidos = ["bista","holfato","takto","guzto","hoido"]
    
# #     def __init__(self,nombre,edad, apellido, profesion) -> None:
# #         self.nombre = nombre
# #         self.edad = edad
# #         self.apellido = apellido
# #         self.profesion = profesion
        
# #     def __str__(self) -> str:
# # #         return f"{self.nombre} tiene {self.edad} años"

# # #     def area_rectangulo(self,
# # #         altura:float,
# # #         base:float,
# # #         nombre:str
# # #     ) -> str:
# # #         area = base * altura
# # #         response = f"{nombre} tiene un rectangulo de area {area}"
# # #         print(response)
        
# # #     def saludo(self):
# # #         print(f"hola {self.nombre} {self.apellido}, ¿como estas?")

# # # p1 = Personas("gabriela","24","giraldo","estudiante")
# # # p2 = Personas("felipe","23","gonzalez","batman")

# # # print(p1.nombre)
# # # print(p2.nombre)

# # # print(p1.area_rectangulo(2,3,"felipe"))
# # # p1.saludo()


class Personas():
    libros = {}
    
    def __init__(self,nombre,apellido,edad,colegio):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad 
        self.colegio = colegio
        # self.libros = {
        #     "nombre":self.nombre,
        #     "apellido":self.apellido,
        #     "edad":self.edad,
        #     "colegio":self.colegio,
        #     "libros":{}
        # }
    def agregar(self,nom_libro,fecha):
        self.libros.update({nom_libro:fecha})


p1 = Personas("felipe","gonzalez","23","BIS")
p2 = Personas("gabriela","gonzalez","23","BIS")

p2.agregar("python","24/02/2023")
p2.agregar("java","12/02/2023")

p1.agregar("docker","24/02/2023")
p1.agregar("aws","12/02/2023")

print(p2.libros)
print("\n")
print(p1.libros)

print("-"*50)

# class Persona: 
# 	# atributos
# 	nombre = "Josune"
# 	edad = 24 
	
# 	# metodos
# 	def camina(self):
# 		print(self.nombre + " está caminando")
  
# p1 = Persona() # la variable p1 contiene un objeto de la clase Persona
# p1.camina()
# print(p1.nombre)  
# print(p1.edad)


# GODOFREDO = Persona() # la variable GODOFREDO contiene un objeto de la clase Persona
# GODOFREDO.camina()
# print(GODOFREDO.nombre)  
# print(GODOFREDO.edad)




class Banco():
    monto = 0
    
    def __init__(self,nombre)->None:
        self.nombre = nombre
        self.monto_persona = 0
    
    def ingresar_dinero(self,dinero):
        self.monto = self.monto + dinero
        self.monto_persona = self.monto_persona + dinero

felipe = Banco("felipe")
felipe.ingresar_dinero(15)
print(felipe.monto_persona)

godofredo = Banco("Godofredo")
godofredo.ingresar_dinero(7)
print(godofredo.monto_persona)
print("-----")
print(felipe.monto)
print(godofredo.monto)




# class Demo:
# 	atrib_estatico = 5 # compartido por todos los objetos
# 	def __init__(self,numero):
# 		self.atrib_instancia = numero # específico de cada objeto

# c1 = Demo(4)
# c2 = Demo(7)

# # Valor inicial
# print(f"C1: Estatico {c1.atrib_estatico} - Instancia: {c1.atrib_instancia}")
# # output: C1: Estatico 123 - Instancia: 456
# print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# # output: C2: Estatico 123 - Instancia: 789

# Demo.atrib_estatico = -1
 
# print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# # output: C2: Estatico -1 - Instancia: 456
# print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# # output: C2: Estatico -1 - Instancia: 789

# c1.atrib_instancia = 999
  
# print(f"C1: Estatico {c1.atrib_estatico} - Instancia: {c1.atrib_instancia}")
# # output: C1: Estatico -1 - Instancia: 999

# print(f"C2: Estatico {c2.atrib_estatico} - Instancia: {c2.atrib_instancia}")
# # output: C2: Estatico -1 - Instancia: 789



# class Coche():
#     def __init__(self,matricula,marca,kilometros, gasolina):
#         self.matricula = matricula
#         self.marca = marca
#         self.kilometros = kilometros #27
#         self.gasolina = gasolina # 300
        
#     def avanzar(self,km): # preguntar cuantos km avanzó
#         if km > self.gasolina:
#             x = -(self.gasolina - km)
#             km2 = km -x
#             self.gasolina = self.gasolina -km2
#             print(f'Te quedaste sin gasolina en el km {x}')
#         else:
#             self.gasolina = self.gasolina - km
#             self.kilometros = self.kilometros + km

# felipe = Coche("QHY451","chevrolet",45,20)
# felipe.avanzar(25)
# print(felipe.gasolina)
# print(felipe.kilometros)

# class Robot():
#     # variable de clase
#     # x = 0
#     # y =0 
#     def __init__(self,x,y,nombre):
#         self.x = x
#         self.y = y
#         self.nombre = nombre 
    
#     def horizontal(self):
#         n = int(input(f"cuantos quiere que se mueva {self.nombre} horizontalmente: "))
#         self.x = self.x + n
    
#     def vertical(self):
#         n = int(input(f"cuantos quiere que se mueva {self.nombre} verticalmente: "))
#         self.y = self.y + n

#     def posicion(self):
#         print(f"{self.nombre} se encuentre en ({self.x},{self.y})")

# robotcito = Robot(0,0,"Humberto")
# robotcito.horizontal()
# robotcito.vertical()
# robotcito.posicion()