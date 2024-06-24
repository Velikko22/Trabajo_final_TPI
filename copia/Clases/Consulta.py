from Diagnostico import Diagnostico
from Mascota import Mascota
from Persona import Personas

import datetime

class Consulta:
    def __init__(self, historialMedico, diagnostico, mascota, veterinario,cliente):
        self.historialMedico = historialMedico
        self.diagnostico = diagnostico
        self.mascota = mascota
        self.veterinario = veterinario
        self.cliente = cliente
        self.fecha = datetime.datetime.now()
        self.fecha_formateada = self.fecha.strftime("%d-%m-%Y %H:%M")


    def crearNuevoHistorial(self):
        lista_consulta = [self.fecha_formateada,self.mascota,self.veterinario,self.cliente,self.diagnostico,self.historialMedico]
        return lista_consulta

    def eliminarHistorial(self):
        pass

    def modificarHistorial(self):
        pass
    def getHistorial(self):
        pass
