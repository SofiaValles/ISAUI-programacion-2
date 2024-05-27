#4. Filtrar diccionario: Escribe una función que reciba un diccionario y una lista de claves,
#y devuelva un nuevo diccionario solo con las claves especificadas.
def Filtrar_Diccionario(dicc,lista):
    nuevo_dicc={}
    for clave,valor in dicc.items():
        if clave in lista:
            nuevo_dicc[clave]= valor
    return nuevo_dicc

#prueba
dicc={ "a": 1,
    "b": 2,
    "c": 3,
    "d": 4}
lista= {"a": 1,
    "c": 3}
resultado= Filtrar_Diccionario(dicc,lista)
print("Su nuevo dicc. con las claves especificadas es: ", resultado)