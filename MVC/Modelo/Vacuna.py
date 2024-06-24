from datetime import date, timedelta

class Vacuna:
    
    def __init__(self, nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis):
        self.nombreVacuna = nombreVacuna
        self.loteVacuna = int(loteVacuna)
        self.numeroDosis = int(numeroDosis)
        self.fechaDosis = date.today()
        self.proximaDosis = self.fechaDosis + timedelta(days=int(diasProximaDosis))
        self.state = True

    def getNombreVacuna(self):
        return self.nombreVacuna
    
    def getLoteVacuna(self):
        return self.loteVacuna
    
    def getNumeroDosis(self):
        return self.numeroDosis
    
    def getFechaDosis(self):
        return self.fechaDosis
    
    def setNombreVacuna(self, newNombreVacuna):
        self.nombreVacuna = newNombreVacuna
    
    def setLoteVacuna(self, newLoteVacuna):
        self.loteVacuna = newLoteVacuna
    
    def setNumeroDosis(self, newNumeroDosis):
        self.numeroDosis = newNumeroDosis
    
    def setFechaDosis(self, newFechaDosis):
        self.fechaDosis = newFechaDosis
    
    def __str__(self):
        return "STR de la clase Vacuna,\nRecibe: Nombre de la vacuna(STR), Lote de la vacuna(INT), Numero de dosis de la vacuna(INT), Dias faltantes para la proxima dosis(INT)\nMetodos: addVacuna: agrega un vacuna\nmodVacuna: modifica alguna vacuna existente\ndelVacuna: delVacuna no elimina el elemento, solo cambia el estado para que no aparezca\n\nAdemas cuenta con los Getters y los Setters de cada atributo"
    
    def __repr__(self):
        return "REPR de la clase Vacuna"