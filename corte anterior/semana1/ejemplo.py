# llenar con valores del 1 - 20
lista_edades_a =[1,3,6,3,5,7]
lista_edades_b =[24,56,8,2]



def algun_mayor_edad(
    x:list,
    y:list
)-> list:
    
    nuevalista= x+y
    lista_mayoredad=[]
    for i in nuevalista:
        if i >18: 
            print(i)
            lista_mayoredad.append(i)
    len(lista_mayoredad)
    print(len(lista_mayoredad))
            
    print(lista_mayoredad)
    # funcion que me sume dos listas de edades 
    # que me indique cuantos mayores de edad hay
    
    # return f"hay {mayores_edad} mayores de edad en la clase"
algun_mayor_edad(lista_edades_a,lista_edades_b)