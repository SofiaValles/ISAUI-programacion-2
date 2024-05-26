#5. Eliminar duplicados: Crea una función que tome una lista y devuelva una nueva lista
#sin elementos duplicados.

def Eliminar_Duplicados(lista):
    listanueva=[]
    listanueva= (set(lista))
    return(listanueva)

#prueba
lista=[1,1,2,2,3,4,5]
resultado= Eliminar_Duplicados(lista)
print("La lista sin repetidos es: ", resultado)