from producto import Producto # Importación de la clase Producto desde el módulo producto

#se definen las variables
fecha_expiracion="eee"
nombre=""
precio=""
cantidad=""

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
        print("\n"+"Los datos de su alimento son: "+ "\nFecha de expiración: " + str(self.getFecha_expiracion())+"\n")


# Creación de una instancia de la clase Alimento con los datos proporcionados
resultado= Alimento(nombre,precio,cantidad,fecha_expiracion)
# Llamada al método mostrar_informacion_alimento para imprimir los detalles del alimento
resultado.mostrar_informacion_alimento()