# Importación de la clase Producto desde el módulo producto
from producto import Producto

#se definen las variables
marca="ccc"
modelo="ddd"
nombre=""
precio=""
cantidad=""
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
        print("\n"+"Los datos de electrónico son: "+ "\nMarca: " + str(self.getMarca()) + "\nModelo: "+ str(self.getModelo())+"\n")

# Creación de una instancia de la clase Electronico con los datos proporcionados
resultado= Electronico(nombre,precio,cantidad,marca,modelo)
# Llamada al método mostrar_informacion_electronico para imprimir los detalles del producto electrónico
resultado.mostrar_informacion_electronico()