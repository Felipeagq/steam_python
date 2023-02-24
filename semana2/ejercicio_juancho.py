def operacion_listas(
   
):
    
    numerito= int(input("Dijita el numero de palabras de la lista "))
    lista = []
    for i in range(numerito):
        palabra=input(f"Dijita palabra {i+1} : ")
        lista.append(palabra)
    
    
    numerito2= int(input("Dijita el numero de palabras de la lista "))
    lista2 = []
    for j in range(numerito2):
        palabra=input(f"Dijita palabra que deseas remove {j+1} : ")
        lista2.append(palabra)
    
    print(lista)
    print(lista2)
    
    for k in lista2:
        if k in lista:
            lista.remove(k)
    
    print("lista final: ",lista)
    
        






operacion_listas()
        
    