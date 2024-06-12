# Importación de la clase Producto desde el módulo producto
from producto import Producto

# Definición de la clase Electronico que hereda de la clase Producto
class Electronico(Producto):
    def __init__(self,nombre,precio,cantidad,marca,modelo):
         # Llamada al constructor de la clase padre (Producto) para inicializar los atributos comunes
        super().__init__(nombre,precio,cantidad)
         # Inicialización de los atributos específicos de Electronico (marca y modelo)
        self.marca= marca
        self.modelo= modelo

# Métodos para obtener la marca y el modelo del producto electrónico
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
  # Método para mostrar la información del producto electrónico
    def mostrar_informacion_electronico(self):
        print("\n"+"Los datos de electrónico son: "+ "\n Nombre: " + str(self.getNombre())+ "\n Precio: " +str(self.getPrecio())+ "\n Cantidad: " + str(self.getCantidad())+ "\n Marca: " + str(self.getMarca()) + "\n Modelo: "+ str(self.getModelo())+"\n")
