#Ejercicio 8: Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario.
 #La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), 
#números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.
import random
numero = random.choice
#Ejercicio 8: Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario.
#La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de letras (mayúsculas y minúsculas), 
#números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.

import random
contrasena= ""
#for
minus = random.choice(["a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z,"])
mayus=random.choice(["A,B,C,D,E,F,G,H,I,J,K,L,M,N,Ñ,O,P,Q,R,S,T,U,V,W,X,Y,Z"])
numero=random.choice(["0,1,2,3,4,5,6,7,8,9"])
#especial=random.choice([!,¡,?,¿,*,@ ])
                        


contrasena = len()
while len(contrasena)>=12:
    contrasena = minus + mayus + numero
    
print(contrasena)

#ejercicio 6
'''#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial 
#(por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.'''

import re

def validar_contrasena(contrasena):
    # Longitud mínima de 8 caracteres
    if len(contrasena) < 8:
        return False
    
    # Al menos una letra mayúscula, una letra minúscula, un número y un carácter especial
    if not re.search('[A-Z]', contrasena):
        return False
    if not re.search('[a-z]', contrasena):
        return False
    if not re.search('[0-9]', contrasena):
        return False
    if not re.search('[!@#$%^&*()\-_=+{};:,<.>]', contrasena):
        return False
    
    return True

# Solicitar contraseña al usuario
contrasena = input("Por favor, ingrese su contraseña: ")

# Validar la contraseña ingresada
if validar_contrasena(contrasena):
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")


