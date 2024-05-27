#3. Merge de diccionarios: Crea una función que tome dos diccionarios y devuelva uno
#nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
#diccionario).
def Merge_Diccionarios (dicc1,dicc2):
    dicc_Nuevo= dicc1 | dicc2
    return dicc_Nuevo

#prueba
dicc1={"hola"}
dicc2={"chau"}
resultado= Merge_Diccionarios(dicc1,dicc2)
print("El contenido de su nuevo diccionario es: ", resultado)