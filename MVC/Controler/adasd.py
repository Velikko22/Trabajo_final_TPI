
                    
#############################################################################
        
    def agregarMascota(self):
        tipo_de_animal = input("Ingrese tipo de animal: ").lower()
        tipo_de_raza = input("Ingrese el nombre de la Raza: ").lower()
        if self.controladorRaza.validarRaza(tipo=tipo_de_animal, raza=tipo_de_raza):
            identificador = input("Ingrese ID mascota: ").lower()
            propietario = input("Ingrese nombre propietario: ").lower()
            nombreAnimal = input("Ingrese nombre del animal: ").lower()
            detalleMascota = input("Ingrese Detalle Mascota: ").lower()
            stateMascota = self.controladorRaza.validarIngresoState()

            linea = f"{tipo_de_animal};{tipo_de_raza};{identificador};{propietario};{nombreAnimal};{detalleMascota};{stateMascota}"
            nombre_archivo = f"{identificador}_{propietario}.txt"
            lugar_y_nombre_archivo = RUTA_MASCOTAS / nombre_archivo

            with lugar_y_nombre_archivo.open("w", encoding="UTF-8") as file:
                file.write(linea)
                print("Archivo creado y guardado.")

            self.lista_mascotas_objeto = []
            self.cargarArchivoMascota()

    def buscarMascota(self):
        buscar_nombre_mascota = input("Ingrese nombre mascota: ")
        buscar_nombre_propietario = input("Ingrese nombre propietario: ")
        for mascota in self.lista_mascotas_objeto:
            if mascota.nombreAnimal == buscar_nombre_mascota and mascota.propietario == buscar_nombre_propietario and mascota.mascotaActiva():
                print(mascota)

    def modificarMascota(self):
        id_mascota = input("Ingrese el ID de la mascota: ")
        propietario = input("Ingrese el nombre del propietario: ")

        archivo_a_buscar = f"{id_mascota}_{propietario}.txt"
        archivo_path = RUTA_MASCOTAS / archivo_a_buscar
        if not archivo_path.exists():
            print("ERROR: EL ARCHIVO NO EXISTE")
            print("REGRESANDO A MENU...")
            return

        with open(archivo_path, "r", encoding="UTF-8") as file:
            linea = file.readline()
            tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, historial, stateMascota = linea.strip().split(";")
        mascota_objeto = Mascota(tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, historial, stateMascota)
        self.lista_mascotas_objeto.append(mascota_objeto)

        while True:
            try:
                print("===============")
                print("Que desea modificar?")
                print("1 Tipo Animal\n2 Nombre Raza\n3 Identificador Mascota\n4 Nombre Propietario\n5 Nombre Mascota\n6 Historial\n7 Estado Mascota\n0 Salir y Guardar cambios")
                opcion = int(input("?... "))

                if opcion == 1:
                    nuevo_tipo = input("Nuevo tipo: ").lower()
                    mascota_objeto.set_tipoAnimalRaza(nuevo_tipo)
                elif opcion == 2:
                    nuevo_nombre_raza = input("Nuevo nombre de raza: ").lower()
                    mascota_objeto.set_nombreRazaAnimal(nuevo_nombre_raza)
                elif opcion == 3:
                    nuevo_identificador = input("Nuevo identificador: ").lower()
                    mascota_objeto.set_identificador(nuevo_identificador)
                elif opcion == 4:
                    nuevo_propietario = input("Nuevo propietario: ").lower()
                    mascota_objeto.set_propietario(nuevo_propietario)
                elif opcion == 5:
                    nuevo_nombreAnimal = input("Nuevo nombre de animal: ").lower()
                    mascota_objeto.set_nombreAnimal(nuevo_nombreAnimal)
                elif opcion == 6:
                    nuevo_historial = input("Nuevo historial: ").lower()
                    mascota_objeto.set_historial(nuevo_historial)
                elif opcion == 7:
                    nuevo_stateMascota = input("Nuevo estado de mascota: ").lower()
                    mascota_objeto.set_stateMascota(nuevo_stateMascota)
                elif opcion == 0:
                    if self.controladorRaza.validarRaza(mascota_objeto.get_tipoAnimalRaza(), mascota_objeto.get_nombreRazaAnimal()):
                        archivo_path.unlink()
                        nuevo_nombre_archivo = f"{mascota_objeto.get_identificador()}_{mascota_objeto.get_propietario()}.txt"
                        nuevo_archivo_path = RUTA_MASCOTAS / nuevo_nombre_archivo
                        with open(nuevo_archivo_path, "w", encoding="UTF-8") as file:
                            file.write(f"{mascota_objeto.get_tipoAnimalRaza()};{mascota_objeto.get_nombreRazaAnimal()};"
                                       f"{mascota_objeto.get_identificador()};{mascota_objeto.get_propietario()};"
                                       f"{mascota_objeto.get_nombreAnimal()};{mascota_objeto.get_historial()};"
                                       f"{mascota_objeto.get_stateMascota()}")
                        print("Cambios guardados exitosamente.")
                        self.lista_mascotas_objeto = []
                        self.cargarArchivoMascota()
                        break
                    else:
                        print("La raza modificada no existe. No se guardaron los cambios. Debe crearla!")
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def iniciarCarga(self):
        self.controladorRaza.cargarArchivoRaza()
        self.controladorMascota.cargarArchivoMascota()

    def mostrarMenu(self):
        while True:
            self.vistaMenuRazaMascota.mostrarOpcionesMenuRaza()
            opcion_menu = int(input("Ingrese opcion: "))
            if opcion_menu == 1:
                print(self.controladorRaza.lista_razas_objetos)
                self.controladorRaza.listarRazasDisponibles()
            elif opcion_menu == 2:
                self.controladorRaza.buscarRaza()
            elif opcion_menu == 3:
                self.controladorRaza.modificarRaza()
            elif opcion_menu == 4:
                self.controladorRaza.agregarRaza()
            elif opcion_menu == 5:
                self.controladorRaza.eliminarRaza()
            elif opcion_menu == 6:
                self.controladorMascota.buscarMascota()
            elif opcion_menu == 7:
                self.controladorMascota.agregarMascota()
            elif opcion_menu == 8:
                self.controladorMascota.modificarMascota()

    def cargarArchivoRaza(self):
        archivos = list(RUTA_RAZAS.glob('*'))
        for archivo in archivos:
            with open(archivo, "r", encoding="UTF-8") as file:
                linea = file.readline()
                tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaRaza = linea.strip().split(";")
                self.lista_razas_objetos.append(Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaRaza))

###############################################################################

# diagnostico

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
    
    def cambiarState(self):
        if self.state:
            self.state = False
        else:
            self.state = True

# trataminto

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
            
    def cambiarState(self):
        try:
            if self.state:
                self.state = False
            else:
                self.state = True
        except:
            return "Error al cambiar el estado"
    
    def NombreTratamiento(self, newNombre):
        try:
            self.nombreTratamiento = newNombre
        except:
            return "Error al cambiar de nombre"
    
    def DuracionTratamiento(self, newDuracion):
        try:
            self.duracionTratamiento = newDuracion
        except:
            return "Error al cambiar la duracion del tratamiento"
# Vacunacion

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

###############################################################################

    