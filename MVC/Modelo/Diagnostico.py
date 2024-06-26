
class Diagnostico:
    
    def __init__(self, nombreDiag, descripcionDiag, cuidadosDiag, state = True):
        self.nombreDiag = nombreDiag
        self.descripcionDiag = descripcionDiag
        self.cuidadosDiag = cuidadosDiag
        #self.tratamientoDiag = tratamientoDiag
        #self.vacunasDiag = vacunasDiag
        self.state = state





    def getNombreDiag(self):
        return self.nombreDiag
    
    def getDescripcionDiag(self):
        return self.descripcionDiag
    
    def getCuidadosDag(self):
        return self.cuidadosDiag


    

    def getState(self):
        return self.state
    
    def setNombreDiag(self, newNombreDiag):
        self.nombreDiag = newNombreDiag
    
    def setDescripcionDiag(self, newDescripcionDiag):
        self.descripcionDiag = newDescripcionDiag
    
    def setCuidadosDag(self, newCuidadosDiag):
        self.cuidadosDiag = newCuidadosDiag

    def setstate(self,state):
        self.state = state


    
    def __str__(self):
        return f"{self.nombreDiag},{self.descripcionDiag},{self.cuidadosDiag},{self.state}"
    
    def __repr__(self):
        return f"{self.nombreDiag},{self.descripcionDiag},{self.cuidadosDiag},{self.tratamientoDiag},{self.vacunasDiag},{self.state}"


