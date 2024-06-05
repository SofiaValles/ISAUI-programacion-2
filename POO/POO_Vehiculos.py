#POO_Vehiculos
'''
Crear un programa que permita crear la clase vehículo, capaz de procesar la información básica 
de de los vehículos de un consecionario.  Suponga que los atributos de un vehículo son: 
marca, patente, modelo, kilometraje 
'''
Vehiculo=""
class Vehiculo():
    def __init__(self, marca, patente, modelo, kilometraje):
        self.marca= marca
        self.patente=patente
        self.modelo=modelo
        self.kilometraje= kilometraje

    #metodos de acceso
    def getPatente(self):
        return self.patente
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getKilometraje(self):
        return self.kilometraje
    
    def mostrarInfoVehiculo(self):
        print("\n"+ "Los datos ingresados son: " +  "\n Patente: " + str(self.getPatente()) + "\n Marca: "+ str(self.getMarca()) + "\n Modelo: "+ str(self.getModelo()) + "\n Kilometraje: "+ str(self.getKilometraje())+ " km" )

patente= input("Ingrese la patente: ")
marca= input("Ingrese la marca: ")
modelo= input("Ingrese el modelo: ")
kilometraje= input("Ingrese el kilometraje: ")

resultado= Vehiculo(marca, patente, modelo, kilometraje) #añadir todos los parametros
resultado.mostrarInfoVehiculo()