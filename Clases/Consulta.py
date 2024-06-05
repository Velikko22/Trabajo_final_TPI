import Diagnostico

class Consulta:
    def __init__(self, historialMedico):
        self.historialMedico = historialMedico
        self.tratamiento = Diagnostico.Tratamientos("NombreDelTratamiento", "DiasDelTratamiento")
        self.vacuna = Diagnostico.Vacuna("NombreDeLaVacuna", 4, 3, 10)
        self.diagnostico = Diagnostico.Diagnostico("NombreDiagnostico", "DescripcionDiagnostico", "CuidadosDiagnostico", self.tratamiento, self.vacuna)
    def crearNuevoHistorial(self):
        pass
    def eliminarHistorial(self):
        pass
    def modificarHistorial(self):
        pass
    def getHistorial(self):
        pass
