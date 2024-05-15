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


#Ejercicio 8: Generador sde Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario.
 #La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), 
#números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.
import random

minus = random.choices("abcdefghijklmnopqrstuvwxyz")
mayus= random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
numero = random.choices("0123456789")
especial = random.choices("[!,¡?¿*@.;:]")

largocontra= random.randint(12,16) 
contrasena=""  

def aleatorio():
    minus = random.choices("abcdefghijklmnopqrstuvwxyz")
    mayus= random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numero = random.choices("0123456789")
    especial = random.choices("[!,¡?¿*@.;:]")
    contrasena += random.choice(minus + mayus + numero + especial)



for i in range(largocontra):
    minus = random.choices("abcdefghijklmnopqrstuvwxyz")
    mayus= random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numero = random.choices("0123456789")
    especial = random.choices("[!,¡?¿*@.;:]")
    contrasena += random.choice(minus + mayus + numero + especial)

   

while len(contrasena)<12:
    contrasena += random.choice(minus + mayus + numero + especial)
                        
print(contrasena)