#1. Contar letras: Escribe una función que reciba una cadena y devuelva un diccionario
#con la frecuencia de cada letra en la cadena.
def Cadena_a_Diccionario(cadena):
    diccionario= {}
    for letra in cadena:
        if letra in diccionario:
            diccionario[letra]+=1
        else:
            diccionario[letra]=1
    return diccionario
#prueba
cadena = "ejemplo"
resultado = Cadena_a_Diccionario(cadena)
print(resultado)