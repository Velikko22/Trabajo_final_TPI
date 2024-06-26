
class Diagnostico:
    
    def __init__(self, nombreDiag, descripcionDiag, cuidadosDiag, tratamientoDiag, vacunasDiag, state = True):
        self.nombreDiag = nombreDiag
        self.descripcionDiag = descripcionDiag
        self.cuidadosDiag = cuidadosDiag
        self.tratamientoDiag = tratamientoDiag
        self.vacunasDiag = vacunasDiag
        self.state = state

    numeroDiagnostico = None
    def getNumDiag(self):
        return self.numeroDiagnostico

    def setNumDiag(self,numeroDiagnostico):
        self.numeroDiagnostico = numeroDiagnostico
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
        return f"{self.nombreDiag},{self.descripcionDiag},{self.cuidadosDiag},{self.tratamientoDiag.nombreTratamiento},{self.vacunasDiag.nombreVacuna},{self.state}"
    
    def __repr__(self):
        return f"{self.nombreDiag},{self.descripcionDiag},{self.cuidadosDiag},{self.tratamientoDiag},{self.vacunasDiag},{self.state}"


