#Diccionario de frecuencias: Escribe una función que reciba una lista de palabras y
#devuelva un diccionario con la frecuencia de cada palabra.
def diccionario_de_frecuencias(lista_palabras):
    frecuencias = {}
    for palabra in lista_palabras:
        if palabra in frecuencias:
            frecuencias[palabra] += 1
        else:
            frecuencias[palabra] = 1
    return frecuencias
