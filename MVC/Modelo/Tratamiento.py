class Tratamiento:
    def __init__(self, nombreTratamiento, duracionTratamiento, state):
        self.nombreTratamiento = nombreTratamiento
        self.duracionTratamiento = duracionTratamiento
        self.state = state

    def tratamientoActivo(self):
        if self.state == 1:
            return True

    def getNombreTratamiento(self):
        return self.nombreTratamiento

    def getDuracionTratamiento(self):
        return self.duracionTratamiento

    def getState(self):
        return self.state

    def setNombretratamiento(self, nombretratamiento):
        self.nombreTratamiento = nombretratamiento

    def setDuracionTratamiento(self, duracionTratamiento):
        self.duracionTratamiento = duracionTratamiento

    def setState(self, state):
        self.state = state

    def __str__(self):
        return (f"{self.nombreTratamiento}, {self.duracionTratamiento}, {self.state}")

    def __repr__(self):
        return (f"{self.nombreTratamiento}, {self.duracionTratamiento}, {self.state}")