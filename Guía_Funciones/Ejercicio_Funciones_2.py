#Ejercicio 2
#Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
#valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
#máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    Maximo= max(lista)
    Minimo= min(lista)
    return(Maximo, Minimo)

lista= input("Ingrese una lista de números para calcular el mayor y menor (todo junto, sin comas ni espacios): ")
resultado= calcularMaxMin(lista)
print("Su máximo y minimos son, respectivamente: ", resultado)