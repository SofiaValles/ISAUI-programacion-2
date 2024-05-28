#Agrupar por longitud: Escribe una función que reciba una lista de palabras y devuelva
#un diccionario donde las claves son las longitudes de las palabras y los valores son
#listas de palabras con esa longitud.
def agrupar_por_longitud(lista_palabras):
    resultado = {}
    for palabra in lista_palabras:
        longitud = len(palabra)
        if longitud in resultado:
            resultado[longitud].append(palabra)
        else:
            resultado[longitud] = [palabra]
    return resultado

# Ejemplo de uso:
palabras_ejemplo = ["manzana", "naranja", "pera", "banana", "kiwi", "uva", "limón"]
resultado_ejemplo = agrupar_por_longitud(palabras_ejemplo)
print(resultado_ejemplo)