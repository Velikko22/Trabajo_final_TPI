class Tratamientos:
    def __init__(self, nombreTratamiento, duracionTratamiento):
        self.nombreTratamiento = nombreTratamiento
        self.duracionTratamiento = duracionTratamiento
    def addTratamiento(self, newNombre, newDuracion):
        with open("Datos archivos.txt\Tratamiento.txt", 'a') as archivo:
            nueva_linea = newNombre + "," + newDuracion + "\n"
            archivo.write(nueva_linea)
    def getNombreTratamiento(self):
        return self.nombreTratamiento
    def getDuracionTratamiento(self):
        return self.duracionTratamiento
    def setNombreTratamiento(self, newNombre):
        self.nombreTratamiento = newNombre
    def setDuracionTratamiento(self, newDuracion):
        self.duracionTratamiento = newDuracion
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

if __name__=="__main__":
    prueba = Tratamientos("Caca", "3 Dias")
    prueba.addTratamiento("caca", "3 Dias")