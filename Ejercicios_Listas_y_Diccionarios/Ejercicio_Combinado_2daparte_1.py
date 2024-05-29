#1 Notas de estudiantes : Escribe una función que recibe un diccionario donde las claves son nombres
# de estudiantes y los valores son listas de sus calificaciones. La función debe devolver un nuevo 
#diccionario con las mismas claves pero donde los valores son la calificación promedio de cada estudiante.
def Notas_estudiantes(dicc):
    nuevodicc={}
    for clave,valor in dicc.items():
        prom=sum(valor)/len(valor)
        nuevodicc[clave]= prom
    return nuevodicc

dicc={"pepe": [1,2,3],"moni":[4,5,6],"coqui":[7,8,9],"paola":[4,7,9],"fatiga":[10,10,10]}
res=Notas_estudiantes(dicc)
print(res)