class SerVivo():
    sentidos_lista = ["olfato","vista","oido","gusto","tacto"]
    
    def sentidos(self):
        print(self.sentidos_lista)

    def respirar(self):
        print(f"está respirando")
    
    def sonido(self):
        print("emite un sonido")
    
    def movimiento(self):
        print("se está movimiendo")

# ---------------------------------------


class Persona(SerVivo):
    def __init__(self,nombre):
        self.nombre = nombre
    

p1 = Persona("felipe")
p1.sentidos()
p1.respirar()
p1.movimiento()
p1.sonido()