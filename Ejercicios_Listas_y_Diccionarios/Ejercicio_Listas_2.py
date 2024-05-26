#2. Máximo y mínimo: Escribe una función que reciba una lista de números y devuelva el
#valor máximo y el mínimo de la lista.
def Maximo_Minimo(lista):
    maximo= max(lista)
    minimo= min(lista)
    return maximo, minimo
#prueba
lista=[1,2,3,4,5,6]
resultado= Maximo_Minimo(lista)
print("Los valores máximos y mínimos son:", resultado, "respectivamente")