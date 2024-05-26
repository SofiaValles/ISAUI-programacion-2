#10.Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
#índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.
def Encontrar_Indice(lista, valor):
    cont=0
    indice=-1
    for elemento in lista:
        if elemento == valor:
            indice= cont
            break
        cont+=1 
    return indice

#prueba
lista= [1,2,3,4,5,3]
valor= 3
resultado= Encontrar_Indice(lista, valor)
print("Su índice es: ", resultado)