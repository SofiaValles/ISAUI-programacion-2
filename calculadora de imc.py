#Solicita al usuario que ingrese su peso en kilogramos.
#Solicita al usuario que ingrese su altura en metros.
#Calcula el IMC utilizando la fórmula proporcionada.
#Muestra el resultado al usuario.

imc=0
kilos= float(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su altura en m: "))
if (altura> 2.5 ):
    altura /= 100

imc= kilos / (altura**2)
print("Su IMC es: ", imc)