#10.Valores únicos: Escribe una función que reciba un diccionario y devuelva una lista de
#valores únicos en el diccionario.
def valores_unicos(diccionario):
    valores_unicos = set()
    for valor in diccionario.values():
        valores_unicos.add(valor)
    return list(valores_unicos)