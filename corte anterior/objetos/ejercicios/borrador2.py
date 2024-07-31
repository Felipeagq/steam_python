class SerVivo():
    ciclo_de_vida = ["dormir","comer","evacuar"]
    
    def __init__(self,nombre):
        self.nombre = nombre
        print(f"{self.nombre} se ha creado")
        
    def sonido(self,clase_sonido):
        self.clase_sonido = clase_sonido
        print(f"esta haciendo un sonido {clase_sonido}")
    
    def movimiento(self):
        print("se está moviendo")

s1 = SerVivo("socrates")
s1.sonido("ahhh")
s1.movimiento()

class Persona(SerVivo):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def movimiento(self):
        return super().movimiento()
    
    def sonido(self):
        super().sonido("uauauau")
        print(f"esta aziendo un zonido de {super().clase_sonido}")
        
    def ciclo(self):
        print(f"el ciclo de vida de mi persona es {super().ciclo_de_vida}")
        


print("-"*50)
p1 = Persona("Jack el destripador")
p1.sonido()
p1.ciclo()