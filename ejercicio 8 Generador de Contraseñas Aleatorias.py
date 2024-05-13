#Ejercicio 8: Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario.
 #La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), 
#números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.

import random

minus = random.choices("abcdefghijklmnopqrstuvwxyz")
mayus= random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numero = random.choices("0123456789")
especial = random.choices("[!,¡?¿*@.;:]")

largocontra= random.randint(12,16) 
contrasena= '' 

for i in range(largocontra):
    contrasena += random.choice(minus + mayus + numero + especial)

while len(contrasena)<12:
    
    contrasena += random.choice(minus + mayus + numero + especial)
                        
print(contrasena)
