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
            nueva_linea = newnombreVacuna + "," + newloteVacuna + "," + newnombreVacuna + "," + str(newnumeroDosis) + "," + newfechaDosis + ",state = 0\n"
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
    def __str__(self):
        return "STR"
    def __repr__(self):
        return "REPR"

if __name__=="__main__":
    a=Vacuna("vacuna", "a44", 1, "24/05/2024")
    #a.addVacuna("vacuna", "a44", 1, "24/05/2024")
    a.modVacuna("a44", "b55")