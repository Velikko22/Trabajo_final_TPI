from datetime import date, timedelta

class Vacuna:
    
    def __init__(self, nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis,state):
        self.nombreVacuna = nombreVacuna
        self.loteVacuna = loteVacuna
        self.numeroDosis = int(numeroDosis)
        self.fechaDosis = date.today()
        self.diasProximaDosis = diasProximaDosis
        self.proximaDosis = self.fechaDosis + timedelta(days=int(diasProximaDosis))
        self.state = int(state)

    def getNombreVacuna(self):
        return self.nombreVacuna
    
    def getLoteVacuna(self):
        return self.loteVacuna
    
    def getNumeroDosis(self):
        return self.numeroDosis
    
    def getFechaDosis(self):
        return self.fechaDosis

    def getstate(self):
        return self.state

    def setNombreVacuna(self, newNombreVacuna):
        self.nombreVacuna = newNombreVacuna
    
    def setLoteVacuna(self, newLoteVacuna):
        self.loteVacuna = newLoteVacuna
    
    def setNumeroDosis(self, newNumeroDosis):
        self.numeroDosis = newNumeroDosis

    def setdiasProximaDosis(self, diasProximaDosis):
        self.diasProximaDosis = diasProximaDosis

    def setFechaDosis(self, newFechaDosis):
        self.fechaDosis = newFechaDosis

    def setstate(self, state):
        self.state = state
    
    def __str__(self):
        return f"{self.nombreVacuna}, {self.loteVacuna}, {self.numeroDosis}, {self.proximaDosis},{self.state}"
    
    def __repr__(self):
        return f"{self.nombreVacuna}, {self.loteVacuna}, {self.numeroDosis}, {self.proximaDosis},{self.state}"