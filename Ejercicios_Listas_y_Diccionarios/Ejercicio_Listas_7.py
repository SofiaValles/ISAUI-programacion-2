#7. Invertir lista: Escribe una función que tome una lista y devuelva una nueva lista con los
#elementos en orden inverso.
def Invertir_Lista(lista):
    return lista[::-1]
    
#prueba
lista= [1,6,2,3,4,5,9]
alreves= Invertir_Lista(lista)
print("su nueva lista invertida es: ", alreves)
