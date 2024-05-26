#4. Elementos mayores que un valor: Escribe una función que tome una lista de números y un valor n,
# y devuelva una nueva lista con los elementos mayores que n.

def ElementosMayores(lista,valorn):
    mayor=[]
    for elemento in lista:
        if elemento > valorn:
            mayor.append(elemento)
    else:
        print("Los elementos no son mayores que n")
    return(mayor)

#prueba
numeros = [1, 2, 3, 4, 5, 6, 7]
n = 3
resultados = ElementosMayores(numeros, n)
print("Elementos mayores que", n, ":", resultados)