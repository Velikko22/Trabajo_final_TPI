
class Diagnostico:
    
    def __init__(self, nombreDiag, descripcionDiag, cuidadosDiag, tratamientoDiag, vacunasDiag):
        self.nombreDiag = nombreDiag
        self.descripcionDiag = descripcionDiag
        self.cuidadosDiag = cuidadosDiag
        self.tratamientoDiag = tratamientoDiag
        self.vacunasDiag = vacunasDiag
        self.state = True
     
    def getNombreDiag(self):
        return self.nombreDiag
    
    def getDescripcionDiag(self):
        return self.descripcionDiag
    
    def getCuidadosDag(self):
        return self.cuidadosDiag
    
    def getTratamientoDiag(self):
        return self.tratamientoDiag
    
    def getVacunasDiag(self):
        return self.vacunasDiag
    
    def getState(self):
        return self.state
    
    def setNombreDiag(self, newNombreDiag):
        self.nombreDiag = newNombreDiag
    
    def setDescripcionDiag(self, newDescripcionDiag):
        self.descripcionDiag = newDescripcionDiag
    
    def setCuidadosDag(self, newCuidadosDiag):
        self.cuidadosDiag = newCuidadosDiag
    
    def setTratamientoDiag(self, newTratamientoDiag):
        self.tratamientoDiag = newTratamientoDiag
    
    def setVacunasDiag(self, newVacunasDiag):
        self.vacunasDiag = newVacunasDiag
    
    def __str__(self):
        return "STR"
    
    def __repr__(self):
        return "REPR"

