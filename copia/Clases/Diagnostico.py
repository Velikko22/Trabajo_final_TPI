from datetime import date, timedelta

class Diagnostico:
    def __init__(self, nombreDiag, descripcionDiag, cuidadosDiag, tratamientoDiag, vacunasDiag):
        self.nombreDiag = nombreDiag
        self.descripcionDiag = descripcionDiag
        self.cuidadosDiag = cuidadosDiag
        self.tratamientoDiag = tratamientoDiag
        self.vacunasDiag = vacunasDiag
        self.state = True
    def addDiagnostico(self, newNombreDiag, newDescripcionDiag, newCuidadosDiag, newTratamientoDiag, newVacunasDiag):
        try:
            with open("Datos archivos.txt/Diagnosticos.txt", 'a') as archivo:
                nombreTratamiento = newTratamientoDiag.nombreTratamiento
                nombreVacuna = newVacunasDiag.nombreVacuna
                nueva_linea = newNombreDiag + "," + newDescripcionDiag + "," + newCuidadosDiag + "," + nombreTratamiento + "," + nombreVacuna + "," + str(self.state) + "\n"
                archivo.write(nueva_linea)
                return "Diagnostico Agregado"
        except:
            return "Error al agregar Diagnostico"
    def modDiagnostico(self):
        pass
    def delDiagnostico(self):
        try:
            if self.state:
                self.state = False
            else:
                self.state = True
        except:
            return "Error al eliminar el Diagnostico"
    def getListadoDiagnostico():
        listadoTotal = []
        with open ("Datos archivos.txt/Diagnosticos.txt", "r") as diagnostico:
            listado = diagnostico.readlines()
            for i in listado:
                listadoDiagnostico = i.strip().split(",")
                if listadoDiagnostico[0] == "NOMBREDIAGNOSTICOS":
                    pass
                elif listadoDiagnostico[0] == " ":
                    pass
                else:
                    listadoTotal.append(listadoDiagnostico[0])
            if listadoTotal == None:
                return "Agregar Diagnosticos"
            else:
                return listadoTotal
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
    def __init__(self, nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis):
        self.nombreVacuna = nombreVacuna
        self.loteVacuna = int(loteVacuna)
        self.numeroDosis = int(numeroDosis)
        self.fechaDosis = date.today()
        self.proximaDosis = self.fechaDosis + timedelta(days=int(diasProximaDosis))
        self.state = True
    def addVacuna(self, newnombreVacuna, newloteVacuna, newnumeroDosis, newfechaDosis):
        try:
            with open("Datos archivos.txt/Vacunas.txt", 'a') as archivo:
                nueva_linea = str(newnombreVacuna) + "," + str(newloteVacuna) + "," + str(newnombreVacuna) + "," + str(newnumeroDosis) + "," + str(newfechaDosis) + "," + str(self.state) + "\n"
                archivo.write(nueva_linea)
        except:
            return "Error al agregar la vacuna"
    def modVacuna(self, parametroCambiante, newParametro):
        try:
            with open("Datos archivos.txt/Vacunas.txt", 'r+') as archivo:
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
        except:
            return "No se encontro el parametro cambiante"
    def getListadoVacunas():
        listadoTotal = []
        with open ("Datos archivos.txt/Vacunas.txt", "r") as vacunas:
            listado = vacunas.readlines()
            for i in listado:
                listadovacuna = i.strip().split(",")
                if listadovacuna[0] == "TRATAMIENTO":
                    pass
                elif listadovacuna[0] == " ":
                    pass
                else:
                    listadoTotal.append(listadovacuna[0])
            if listadoTotal == None:
                return "Agregar tratamiento"
            else:
                return listadoTotal
    def delVacuna(self):
        try:
            if self.state:
                self.state = False
            else:
                self.state = True
        except:
            return "Error al eliminar la vacuna"
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

class Tratamientos:
    def __init__(self, nombreTratamiento, duracionTratamiento):
        self.nombreTratamiento = nombreTratamiento
        self.duracionTratamiento = duracionTratamiento
        self.state = True
    def addTratamiento(self, newNombre, newDuracion):
        try:
            with open("Datos archivos.txt/Tratamiento.txt", 'a') as archivo:
                nueva_linea = newNombre + "," + newDuracion + "," + str(self.state) + "\n"
                archivo.write(nueva_linea)
                return "Tratamiento Guardado"
        except:
            return "Error al guardar el Tratamiento"
    def delTratamiento(self):
        try:
            if self.state:
                self.state = False
            else:
                self.state = True
        except:
            return "Error al eliminar Tratamiento"
    def getListadoTratamiento():
        listadoTotal = []
        with open ("Datos archivos.txt/Tratamiento.txt", "r") as tratamiento:
            listado = tratamiento.readlines()
            for i in listado:
                listadotratamiento = i.strip().split(",")
                if listadotratamiento[0] == "TRATAMIENTO":
                    pass
                elif listadotratamiento[0] == " ":
                    pass
                else:
                    listadoTotal.append(listadotratamiento[0])
            if listadoTotal == None:
                return "Agregar tratamiento"
            else:
                return listadoTotal
    def getNombreTratamiento(self):
        return self.nombreTratamiento
    def getDuracionTratamiento(self):
        return self.duracionTratamiento
    def getState(self):
        return self.state
    def cambiarState(self):
        try:
            if self.state:
                self.state = False
            else:
                self.state = True
        except:
            return "Error al cambiar el estado"
    def setNombreTratamiento(self, newNombre):
        try:
            self.nombreTratamiento = newNombre
        except:
            return "Error al cambiar de nombre"
    def setDuracionTratamiento(self, newDuracion):
        try:
            self.duracionTratamiento = newDuracion
        except:
            return "Error al cambiar la duracion del tratamiento"
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

if __name__=="__main__":
    Diagnostico.getListadoDiagnostico()