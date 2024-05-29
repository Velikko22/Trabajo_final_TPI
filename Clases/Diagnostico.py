class Diagnostico:
    def __init__(self, nombreDiag, descripcionDiag, cuidadosDiag, tratamientoDiag, vacunasDiag):
        self.nombreDiag = nombreDiag
        self.descripcionDiag = descripcionDiag
        self.cuidadosDiag = cuidadosDiag
        self.tratamientoDiag = tratamientoDiag
        self.vacunasDiag = vacunasDiag
        self.state = True
    def addDiagnostico(self, newNombreDiag, newDescripcionDiag, newCuidadosDiag, newTratamientoDiag, newVacunasDiag):
        with open("Datos archivos.txt\Diagnosticos.txt", 'a') as archivo:
            nombreTratamiento = newTratamientoDiag.nombreTratamiento
            nombreVacuna = newVacunasDiag.nombreVacuna
            nueva_linea = newNombreDiag + "," + newDescripcionDiag + "," + newCuidadosDiag + "," + nombreTratamiento + "," + nombreVacuna + "," + str(self.state) + "\n"
            archivo.write(nueva_linea)
    def modDiagnostico(self):
        pass
    def delDiagnostico(self):
        if self.state:
            self.state = False
        else:
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
    def cambiarState(self):
        if self.state:
            self.state = False
        else:
            self.state = True
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

class Vacuna:
    def __init__(self, nombreVacuna, loteVacuna, numeroDosis, fechaDosis):
        self.nombreVacuna = nombreVacuna
        self.loteVacuna = loteVacuna
        self.numeroDosis = numeroDosis
        self.fechaDosis = fechaDosis
        self.proximaDosis = fechaDosis# + 10 dias ejemplo
        self.state = True
    def addVacuna(self, newnombreVacuna, newloteVacuna, newnumeroDosis, newfechaDosis):
        with open("Datos archivos.txt\Vacunas.txt", 'a') as archivo:
            nueva_linea = newnombreVacuna + "," + newloteVacuna + "," + newnombreVacuna + "," + str(newnumeroDosis) + "," + newfechaDosis + "," + str(self.state) + "\n"
            archivo.write(nueva_linea)
    def modVacuna(self, parametroCambiante, newParametro):
        with open("Datos archivos.txt\Vacunas.txt", 'r+') as archivo:
            linea = archivo.readlines()
            for i in linea:
                elemento = i.strip().split(",")
                if elemento[0] == parametroCambiante:
                    print("nombres")
                    self.nombreVacuna = newParametro
                elif elemento[1] == parametroCambiante:
                    print("lote")
                    self.loteVacuna = newParametro
                elif elemento[2] == parametroCambiante:
                    print("numero")
                    self.numeroDosis = newParametro
                elif elemento[3] == parametroCambiante:
                    print("fecha")
                    self.fechaDosis = newParametro
                elif elemento[4] == parametroCambiante:
                    print("estado")
                    if self.state:
                        self.state = False
                    else:
                        self.state = True
                else:
                    pass
    def delVacuna(self):
        if self.state:
            self.state = False
        else:
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
        return "STR de la clase Vacuna,\nRecibe: Nombre de la vacuna, Lote de la vacuna, Numero de dosis de la vacuna, fecha de dosis de la vacuna\nMetodos: addVacuna: agrega un vacuna\nmodVacuna: modifica alguna vacuna existente\ndelVacuna: delVacuna no elimina el elemento, solo cambia el estado para que no aparezca\n\nAdemas cuenta con los Getters y los Setters de cada atributo"
    def __repr__(self):
        return "REPR de la clase Vacuna"

class Tratamientos:
    def __init__(self, nombreTratamiento, duracionTratamiento):
        self.nombreTratamiento = nombreTratamiento
        self.duracionTratamiento = duracionTratamiento
        self.state = True
    def addTratamiento(self, newNombre, newDuracion):
        with open("Datos archivos.txt\Tratamiento.txt", 'a') as archivo:
            nueva_linea = newNombre + "," + newDuracion + "," + str(self.state) + "\n"
            archivo.write(nueva_linea)
    def delTratamiento(self):
        if self.state:
            self.state = False
        else:
            self.state = True
    def getNombreTratamiento(self):
        return self.nombreTratamiento
    def getDuracionTratamiento(self):
        return self.duracionTratamiento
    def getState(self):
        return self.state
    def cambiarState(self):
        if self.state:
            self.state = False
        else:
            self.state = True
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
    #prueba.addTratamiento("caca", "3 Dias")
    a=Vacuna("vacuna", "a44", 1, "24/05/2024")
    #a.addVacuna("vacuna", "a44", 1, "24/05/2024")
    #a.modVacuna("a44", "b55")
    Diagnostico("nombre diagnostico", "sin descripcion", "cuidados Diagnostico", prueba, a).addDiagnostico("Nombre", "descripcion", "cuidados", prueba, a)