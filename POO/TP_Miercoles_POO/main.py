#Crear una clase padre llamada Producto y dos clases hijas que hereden de ella. Las clases hijas
#deben heredar ciertos atributos de la clase Producto y agregar atributos específicos de cada tipo de
#producto en esas clases hijas, deben estar en otro archivo .py cada una de ellas.
from producto import Producto
from electronico import Electronico
from alimento import Alimento

# Creación de una instancia de la clase Producto con los datos proporcionados
resultado_prod= Producto("Silla","20.000","2")
# Llamada al método mostrar_informacion para imprimir los detalles del producto en pantalla
resultado_prod.mostrar_informacion()

# Creación de una instancia de la clase Electronico con los datos proporcionados
resultado_elect= Electronico("Tablet","200.000","1","Samsung","A7")
# Llamada al método mostrar_informacion_electronico para imprimir los detalles del producto electrónico
resultado_elect.mostrar_informacion_electronico()

# Creación de una instancia de la clase Alimento con los datos proporcionados
resultado_alim= Alimento("Lemon pie","2000","1","24/06/2024")
# Llamada al método mostrar_informacion_alimento para imprimir los detalles del alimento
resultado_alim.mostrar_informacion_alimento()