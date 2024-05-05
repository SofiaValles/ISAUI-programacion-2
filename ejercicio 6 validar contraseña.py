#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.

contrasena= input('Ingrese su contraseña:  \n(Que tenga al menos 8 caracteres, una mayúscula, una minúscula, un número y un caracter especial) ')


if  len(contrasena)>=8:
   # print ("es mayor a 8 caracteres")
    indicador = True