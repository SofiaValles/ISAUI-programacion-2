#Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de
#los números pares en la lista.
def Numeros_Pares(lista):
    sumapares=0
    for elemento in lista:
        if elemento % 2 ==0:
            sumapares= sumapares + elemento
    return sumapares

#prueba
lista= [1,2,3,4,5,6]
resultado= Numeros_Pares(lista)
print("La suma de los pares es: ", resultado)
