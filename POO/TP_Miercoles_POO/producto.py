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
