#2. Diccionario inverso: Escribe una función que tome un diccionario y devuelva uno
#nuevo que invierta las claves y los valores.
def Diccionario_Inverso(diccionario):

    diccionarioNuevo={}

    for clave, valor in diccionario.items():
        diccionarioNuevo[valor] = clave
    return diccionarioNuevo