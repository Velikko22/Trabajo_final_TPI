from Mascota import Mascota
from Veterinarios import Veterinario

import datetime

class FichaMedica:
    def __init__(self, identificador=1):
        self.mascota = Mascota("perro", "caniche","150","yo", "Juli Capellino", "es Feo", "Activo")
        self.veterinario = Veterinario("Yo", "1123453", "ayudante")
        self.historial = None
        self.estado = True
        self.identificador = identificador
        self.fecha = datetime.datetime.now()

    def getFecha(self):
        self.fechaformateada_dias = self.fecha.strftime("%d/%m/%Y")
        self.fechaformateada_horas = self.fecha.strftime("%H:%M")
        return f"el dia es: {self.fechaformateada_dias}, y la hora es: {self.fechaformateada_horas}"
    
    def __str__(self):
        return "Esta es la clase ficha"

if __name__=="__main__":
    a=FichaMedica(1)
    print(a.getFecha())