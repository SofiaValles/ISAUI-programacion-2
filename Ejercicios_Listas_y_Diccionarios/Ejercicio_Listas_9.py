#9. Producto de elementos: Escribe una función que tome una lista de números y
#devuelva el producto de todos los elementos.
def Producto_elementos(lista):
    producto=1
    for elemento in lista:    
        producto= elemento * producto
    return producto


#prueba
lista=[1,2,3,4,5]
resultado= Producto_elementos(lista)
print("su producto es: ", resultado)
