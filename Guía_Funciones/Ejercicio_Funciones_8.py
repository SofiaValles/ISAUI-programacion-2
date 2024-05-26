#8. Concatenar listas: Escribe una función que reciba dos listas y devuelva una nueva lista
#que sea la concatenación de ambas.
def Concatenar_Listas (lista1, lista2):
    nuevalista= lista1 + lista2 
    return nuevalista

#prueba
lista1= [1,2,3]
lista2 =[4,5,6]
resultado = Concatenar_Listas(lista1,lista2)
print("Su lista es: ", resultado)