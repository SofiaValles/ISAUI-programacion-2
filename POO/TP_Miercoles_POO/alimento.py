from producto import Producto # Importación de la clase Producto desde el módulo producto

# Definición de la clase Alimento que hereda de la clase Producto
class Alimento(Producto):
    def __init__(self,nombre,precio,cantidad,fecha_expiracion ):
         # Llamada al constructor de la clase padre (Producto) para inicializar los atributos comunes
        super().__init__(nombre,precio,cantidad)
         # Inicialización del atributo específico de Alimento (fecha_expiracion)
        self.fecha_expiracion= fecha_expiracion
        
    # Método para obtener la fecha de expiración del alimento
    def getFecha_expiracion(self):
        return self.fecha_expiracion
    
     # Método para mostrar la información específica de un alimento
    def mostrar_informacion_alimento(self):
        print("\n"+"Los datos de su alimento son: "+ "\n Nombre: " + str(self.getNombre())+ "\n Precio: " +str(self.getPrecio())+ "\n Cantidad: " + str(self.getCantidad()) + "\n Fecha de expiración: " + str(self.getFecha_expiracion())+"\n")
