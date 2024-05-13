#Ejercicio 9: Calculadora de Factorial 
#Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario.
 #El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n. 
#El programa debe manejar números enteros grandes y mostrar el resultado.

numero = int(input("Ingrese un número entero positivo para calcular la factorial "))
factorial = 1

if numero< 0:
    print("Ingrese un número mayor a cero (positivo)")
    
if numero== 0 or numero== 1:
    print("La factorial es : 1")

else:
     for i in range(1, numero + 1):
            factorial *= i
     print("La factorial es: ", factorial)


    
