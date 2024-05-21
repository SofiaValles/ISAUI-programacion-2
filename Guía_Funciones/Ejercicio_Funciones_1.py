#Guía Ejercicios prácticos de Funciones
#Ejercicio 1
#Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
#cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “.
# Crea un programa principal donde se use dicha función luego del ingreso del usuario.

def ConvertirEspaciado(texto):
    lista = ""
    for letra in texto:
        lista += letra + " "
    return lista


texto = input(¡Hola! Ingrese un texto para agregarle espacios: ")
texto_espaciado = ConvertirEspaciado(texto)
print("Aquí está su texto con espacios adicionales: ", texto_espaciado)
