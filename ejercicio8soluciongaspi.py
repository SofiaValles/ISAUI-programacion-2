#Ejercicio 8: Generador sde Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario.
 #La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), 
#números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.
import random
clave= ""
while len(clave)<12:
    clave+=random.choice("0123456789")
    clave+=random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    clave+=random.choice("abcdefghijklmnopqrstuvwxyz")

    if len(clave)==12:
        break
print(clave)