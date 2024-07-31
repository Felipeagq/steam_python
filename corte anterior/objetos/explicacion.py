class Estudiante():
    def __init__(self,nombre,edad,curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
    
    def aprobo(self,nota):
        if nota > 5:
            return True
        return False


felipe = Estudiante("felipe","23","Python")
print(type(felipe))
print(felipe.aprobo(4))

class Steam():
    def estudiantes(self,estudiantes:Estudiante):
        print({
            "nombre":estudiantes.nombre,
            "edad":estudiantes.edad,
            "curso":estudiantes.curso
        })

s = Steam()
s.estudiantes(felipe)