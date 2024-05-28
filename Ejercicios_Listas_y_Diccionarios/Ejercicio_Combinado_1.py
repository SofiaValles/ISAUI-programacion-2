#Contar palabras en frases: Escribe una función que reciba una lista de frases y
#devuelva un diccionario donde las claves son las palabras y los valores son las
#frecuencias de esas palabras en todas las frases.
def Palabras_en_Frases(lista):
    diccionario = {}
    for frase in lista:
        palabras = frase.split()
        for palabra in palabras:
            if palabra in diccionario:
                diccionario[palabra] += 1
            else:
                diccionario[palabra] = 1
    return diccionario

# Prueba
lista = ["hola buen día", "buenas tardes", "buenas noches"]
resultado = Palabras_en_Frases(lista)
print(resultado)