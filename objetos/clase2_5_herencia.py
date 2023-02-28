class SerVivo():
    sentidos = ["olfato","vista","oido","gusto","tacto"]

class Persona(SerVivo):
    def __init__(self,nombre):
        self.nombre = nombre
    

p1 = Persona("felipe")
print(p1.sentidos)