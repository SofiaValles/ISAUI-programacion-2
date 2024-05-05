#Ejercicio 7: Juego de Adivinar el Número 
#Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo.
# El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo. 
#El juego debe continuar hasta que el jugador adivine correctamente el número.

import random
numero = random.randint(1,100)
guess = 0
while (numero != guess):
    guess = int (input ("Ingrese un número (del 1 al 100) para adivinar: "))
    
    if guess > numero:
        print("el número es menor")

    if guess < numero:
        print("el número es mayor")
            
print("¡Haz adivinado! el número es : ", numero)
