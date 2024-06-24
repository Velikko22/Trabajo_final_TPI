class Tratamiento:
    def __init__(self, nombreTratamiento, duracionTratamiento,state):
        self.nombreTratamiento = nombreTratamiento
        self.duracionTratamiento = duracionTratamiento
        self.state = state

    def getNombreTratamiento(self):
        return self.nombreTratamiento
    
    def getDuracionTratamiento(self):
        return self.duracionTratamiento
    
    def getState(self):
        return self.state
    
    def setNombretratamiento(self,nombretratamiento):
        self.nombreTratamiento = nombretratamiento
        
    def setDuracionTratamiento(self,duracionTratamiento):
        self.duracionTratamiento = duracionTratamiento
    
    def setState(self,state):
        self.state = state
    
    def __str__(self):
        return "STR"
    
    def __repr__(self):
        return "REPR"