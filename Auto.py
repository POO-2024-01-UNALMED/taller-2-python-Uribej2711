class Auto:
    
    cantidadCreados = 0
    
    def __init__ (self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
    
    def cantidadAsientos (self):
        numAsientos = 0
        for asiento in self.asientos:
            if (type(asiento) == asiento):
                numAsientos += 1
        return numAsientos
    def verificarIntegridad(self):
        if(self.registro == self.motor.registro):  
            for asiento in self.asientos:
                if (type(asiento) == asiento):
            
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"             
        
        