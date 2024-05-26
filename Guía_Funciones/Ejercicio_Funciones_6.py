#6. Contar elementos: Escribe una función que reciba una lista y un valor, y devuelva
#cuántas veces aparece ese valor en la lista.

def Contar_Elementos(lista,valor):
    contador=0
    for elemento in lista:
        if elemento==valor:
            contador += 1
    return contador

#prueba
lista=[1,2,3,4,5,5,5]
valor= 5
resultado= Contar_Elementos(lista,valor)
print("el valor elegido aparece:", resultado, "veces")
