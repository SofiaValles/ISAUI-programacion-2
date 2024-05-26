#1. Suma de elementos: Escribe una función que tome una lista de números y devuelva la
#suma de todos los elementos en la lista.
def Suma_de_Elementos(lista):
    suma=0
    for elemento in lista:
        suma=  elemento+suma 
    return suma
#prueba
lista=[1,2,3,4,5]
resultado= Suma_de_Elementos(lista)
print("su suma es: ", resultado)