#3. Promedio de una lista: Crea una función que calcule el promedio de los números en
#una lista dada.

def CalcularPromedio(lista):
    promedio= sum(lista) /len(lista)
    return promedio

#lo siguiente es para comprobar el funcionamiento de la función
numeros = [1, 2, 3, 4, 5, 6]
promedio = CalcularPromedio(numeros)
print("El promedio de sus números es:", promedio)