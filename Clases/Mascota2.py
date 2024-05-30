class Mascota:
    def __init__(self, nombre, propietario, historial, identificador, state):
        self.nombre = nombre
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


    def get_nombre(self):
        return self.nombre

    def set_nombre(self,nombre):
        self.nombre = nombre


    def get_propietario(self):
        return self.propietario

    def set_historial(self, historial):
        self.historial = historial

    def get_historial(self):
        return self.historial

    def set_identificador(self, identificador):
        self.identificador = identificador

    def get_identificador(self):
        return self.identificador

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def __repr__(self):
        return f"{self.nombre}, {self.propietario}, {self.historial},{self.identificador}, {self.state}"
