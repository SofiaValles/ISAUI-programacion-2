#9. Actualizar diccionario: Escribe una función que tome un diccionario y una lista de
#tuplas (clave, valor) y actualice el diccionario con esas tuplas.
def Actualizar_Diccionario(dicc,lista):
    for clave, valor in lista:
        dicc[clave] = valor
