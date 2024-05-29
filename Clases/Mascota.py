class Mascota:
    def __init__(self, nombre, especie, raza, propietario, historial, identificador, state):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.propietario = propietario
        self.historial = historial
        self.identificador = identificador
        self.state = state

    def buscarMascota(self):
        pass
    def altaMascota(self):
        pass
    def modificarMascota(self):
        pass




    def __repr__(self):
        return f"{self.nombre}, {self.especie}, {self.raza}, {self.propietario}, {self.historial},{self.identificador}, {self.state}"
