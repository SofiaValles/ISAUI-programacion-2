#Solicita al usuario que ingrese una temperatura en grados Celsius.
#Convierte la temperatura ingresada a grados Fahrenheit utilizando la fórmula roporcionada.
#Muestra el resultado al usuario.

celsius = float (input("Ingrese una temperatura en grados celsius: "))
fahrenheit =  (celsius * 9/5) + 32
print ("La temperatura es igual a ", fahrenheit, "grados fahrenheit")