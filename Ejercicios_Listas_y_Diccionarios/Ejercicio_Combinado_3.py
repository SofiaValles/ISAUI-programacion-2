#Diccionario de listas: Escribe una función que tome un diccionario donde los valores
#son listas y devuelva una lista que contenga todos los elementos de las listas del
#diccionario.
def Diccionario_de_Listas(dicc):
    elementos=[]
    for lista in dicc.values():
        elementos += lista
    return elementos

