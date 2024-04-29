#Ejercicio 2: Conversor de Moneda
#Desarrolla un programa que convierta una cantidad de dinero de dólares estadounidenses a euros.
#El programa debe solicitar al usuario que ingrese la cantidad en dólares y luego mostrar la cantidad
#equivalente en euros, utilizando un tipo de cambio fijo.

euros = 0.93
dolares = float (input('Ingrese la suma de dinero en dólares: '))
cambio = dolares * euros 

print('Su dinero en euros es: ', round(cambio,2))
