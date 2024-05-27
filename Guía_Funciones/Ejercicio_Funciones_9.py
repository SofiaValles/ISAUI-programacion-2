#Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
#lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.
def Ordenar_Lista_Cadenas(lista):
    listaordenada=[]
    listaordenada= sorted(lista)
    return listaordenada

#prueba 
lista=["a","f","h","z","b"]
resultado= Ordenar_Lista_Cadenas(lista)
print("Su lista ordenada es: ", resultado)