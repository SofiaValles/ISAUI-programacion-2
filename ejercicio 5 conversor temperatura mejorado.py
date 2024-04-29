#Ejercicio 5: Conversor de Temperatura (Actualización)
#Mejora el programa de conversión de temperatura que escribiste anteriormente para que permita 
#al usuario elegir entre convertir de grados Celsius a grados Fahrenheit o viceversa.

opcion= int(input("Ingrese si quiere cambiar de celsius a fahrenheit (INGRESE UN 1), o si quiere cambiar de fahrenheit a celsius (INGRESE UN 2): "))
if opcion == 1:
    celsius = float (input("Ingrese una temperatura en grados celsius: "))
    fahrenheit =  (celsius * 9/5) + 32
    print ("La temperatura es igual a ", fahrenheit, "grados fahrenheit")

if opcion == 2:
    fahrenheit = float(input("Ingrese una temperatura en grados fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print ("La temperatura es igual a ", celsius, "grados celsius")

else:
    print("Ingrese una opción válida porfavor")
