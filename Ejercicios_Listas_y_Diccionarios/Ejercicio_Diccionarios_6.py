#Intercambiar valores: Crea una función que tome un diccionario y dos claves, e
#intercambie los valores de esas dos claves en el diccionario.
def intercambiar_valores(diccionario, clave1, clave2):
    if clave1 in diccionario and clave2 in diccionario:
        diccionario[clave1], diccionario[clave2] = diccionario[clave2], diccionario[clave1]
    else:
        print("Una o ambas claves no existen en el diccionario")
