#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.

#---------------------------------------intento anterior de programa-----------------------------------------------------------------------------------
#import re
#contrasena= input('Ingrese su contraseña:  \n(Que tenga al menos 8 caracteres, una mayúscula, una minúscula, un número y un caracter especial) ')
#if  len(contrasena)>=8:
   # print ("es mayor a 8 caracteres")
    #indicador = True 
#----------------------------------------------------solución----------------------------------------------------------------------------------------
import re

def validar_contrasena(contrasena):
    
    if len(contrasena) < 8:
        return False
    
    # Al menos una letra mayúscula, una letra minúscula, un número y un carácter especial
    if not re.search(r'[A-Z]', contrasena):
        return False
    if not re.search(r'[a-z]', contrasena):
        return False
    if not re.search(r'[0-9]', contrasena):
        return False
    if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', contrasena):
        return False
    
    return True

# Solicitar contraseña al usuario
contrasena = input("Ingrese su contraseña:  \n(Que tenga al menos 8 caracteres, una mayúscula, una minúscula, un número y un caracter especial: ")

# Validar la contraseña ingresada
if validar_contrasena(contrasena):
    print("La contraseña es válida.")
else:
    print("La contraseña no cumple con los requisitos.")




#if  len(contrasena)>=8:
   # print ("es mayor a 8 caracteres")
   # indicador = True


