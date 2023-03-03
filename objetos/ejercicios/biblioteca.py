class Personas():
    
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
