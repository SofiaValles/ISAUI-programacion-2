#Crear una clase padre llamada Producto y dos clases hijas que hereden de ella. Las clases hijas
#deben heredar ciertos atributos de la clase Producto y agregar atributos específicos de cada tipo de
#producto en esas clases hijas, deben estar en otro archivo .py cada una de ellas.

# Se definen las variables para el nombre, precio y cantidad del producto
nombre="aaa"
precio="111"
cantidad="222"

# Definición de la clase padre llamada Producto
class Producto:
    # Constructor de la clase Producto que inicializa los atributos nombre, precio y cantidad
    def __init__(self,nombre,precio,cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad

# Métodos para obtener nombre, precio y cantidad del producto
    def getNombre(self):
        return self.nombre
    def getPrecio(self):
        return self.precio
    def getCantidad(self):
        return self.cantidad
    
    # Método para mostrar la información del producto
    def mostrar_informacion(self):
        print("Los datos ingresados son: "+ "\n Nombre: " + str(self.getNombre())+ "\n Precio: " +str(self.getPrecio())+ "\n Cantidad: " + str(self.getCantidad()))

# Creación de una instancia de la clase Producto con los datos proporcionados
resultado= Producto(nombre,precio,cantidad)
# Llamada al método mostrar_informacion para imprimir los detalles del producto en pantalla
resultado.mostrar_informacion()