#Palabras por letra inicial : Escribe una función que tome una lista de palabras y devuelva 
#un diccionario donde las claves son las letras iniciales de las palabras y los valores 
#son listas de palabras que comienzan con esa letra.
def Palabras_por_Letra_Inicial(lista):
    dicc={}

        #lista=lista.split()
    for palabra in lista:
        primeraletra=palabra[0]
        if primeraletra in dicc:
            dicc[primeraletra].append(palabra)
        else:
            dicc[primeraletra]=[palabra]
    return dicc
#prueba        
lista=["arbol","arroz","chau","hola","no","si"]
res = Palabras_por_Letra_Inicial(lista)
print("resultado: ",res)