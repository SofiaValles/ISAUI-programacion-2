#Ejercicio 1: Calculadora de Promedio
#Escribe un programa en Python que solicite al usuario que ingrese
# tres números y luego calcule y muestre el promedio de esos números.
cantidad = 0
suma = 0
while (cantidad < 3):
    numero = int (input ('Ingrese tres numeros para calcular su promedio: '))
    cantidad= cantidad + 1
    suma = numero + suma

promedio = suma / cantidad
print('Su promedio es: ' , round (promedio))