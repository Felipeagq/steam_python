from clase_2_0 import Banco

felipe = Banco("felipe")
felipe.ingresar_dinero(15)
print(felipe.monto_persona)
godofredo = Banco("Godofredo")
godofredo.ingresar_dinero(7)
print(godofredo.monto_persona)

print(felipe.monto)
print(godofredo.monto)