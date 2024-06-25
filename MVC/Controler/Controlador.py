#region Imports
from Modelo.Cliente import Cliente
from Modelo.Verinario import Veterinario
from Modelo.Mascota import Mascota
from Modelo.Raza import Raza
from Modelo.Diagnostico import Diagnostico
from Modelo.Tratamiento import Tratamiento
from Modelo.Vacuna import Vacuna
from Vista.vista import Vista
#endregion

class Controller:
    
    def __init__(self):
        self.lista_clientes = []
        self.lista_veterinarios = []
        self.lista_mascotas = []
        self.lista_razas = []
        self.lista_diagnostico = []
        self.lista_tratamiento = []
        self.lista_vacuna = []
        self.vista = Vista()

#region Carga de Archivos
    def cargaDatosClientes(self):
        try:
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/clientes.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre = str(datos[0])
                telefono = str(datos[1])
                email = str(datos[2])
                direccion = str(datos[3])
                cantidad = str(datos[4])
                nombreMascota = str(datos[5])
                tipoMascotas = str(datos[6])
                cliente = Cliente(nombre, telefono, email, direccion, cantidad, nombreMascota, tipoMascotas)
                self.lista_clientes.append(cliente)
            self.vista.cargaExitosa("clientes")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de clientes: {str(e)}")
    
    def cargaDatosVeterinarios(self):
        try:
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/veterinarios.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre, telefono, cargo = datos[1], datos[2], datos[3]
                veterinario = Veterinario(nombre, int(telefono), cargo)
                self.lista_veterinarios.append(veterinario)
            self.vista.cargaExitosa("veterinarios")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de veterinarios: {str(e)}")
        
    def cargaDatosMascotas(self):
        try:
            with open("Archivos/mascotas.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, detalleMascota, stateMascota = datos
                mascota = Mascota(tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, detalleMascota, stateMascota)
                self.lista_mascotas.append(mascota)
            self.vista.cargaExitosa("mascotas")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de mascotas: {str(e)}")
        
    def cargaDatosRaza(self):
        try:
            with open("Archivos/raza.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, state = datos
                raza = Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, int(state))
                self.lista_razas.append(raza)
            self.vista.cargaExitosa("raza")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de raza: {str(e)}")
        
    def cargaDatosDiagnostico(self):
        try:
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/Diagnosticos.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombreDiag, descripcionDiag, cuidadosDiag, tratamientoDiag, vacunasDiag = datos
                diagnostico = Diagnostico(nombreDiag, descripcionDiag, cuidadosDiag, tratamientoDiag, vacunasDiag)
                self.lista_diagnostico.append(diagnostico)
            self.vista.cargaExitosa("diagnostico")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de diagnóstico: {str(e)}")
        
    def cargarDatosTratamientos(self):
        try:
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/Tratamiento.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombreTratamiento, duracionTratamiento, state = datos
                tratamiento = Tratamiento(nombreTratamiento, duracionTratamiento, int(state))
                self.lista_tratamiento.append(tratamiento)
            self.vista.cargaExitosa("tratamientos")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de tratamientos: {str(e)}")
    
    def cargaDatosVacunas(self):
        try:
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/Vacunas.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis = datos
                vacuna = Vacuna(nombreVacuna, int(loteVacuna), numeroDosis, diasProximaDosis)
                self.lista_vacuna.append(vacuna)
            self.vista.cargaExitosa("vacunas")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de vacunas: {str(e)}")
#endregion

#region Controlador Historial
    def consulta_Historial(self, nombreCliente, nombreMascota):
        pass
#endregion

#region Controlador Clientes
    def informacion_cliente(self):
        lista = self.lista_clientes
        self.vista.informacionCliente(lista)
    
    def agregar_nuevo_cliente(self):
        nuevoCliente = self.vista.agregarNuevocliente()
        if any(cliente.nombre == nuevoCliente['nombre'] for cliente in self.lista_clientes):
            self.vista.mensajeError("El cliente ya existe.")
        else:
            cliente = Cliente(**nuevoCliente)
            self.lista_clientes.append(cliente)
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/clientes.txt", "a") as archivo:
                archivo.write(f"{nuevoCliente}\n")
            self.vista.cargaExitosa("cliente")
            
   
    def modificar_informacion_Cliente(self):
        nombre_cliente = input("Ingrese el nombre del cliente que desea modificar: ")
    
        cliente_encontrado = None
        for cliente in self.lista_clientes:
            if cliente.nombre.lower() == nombre_cliente.lower():
                cliente_encontrado = cliente
                break
    
        if cliente_encontrado:
            nueva_info_cliente = self.vista.modificarInformacionCliente(cliente_encontrado)
        
        
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/clientes.txt", "r") as archivo:
                lineas = archivo.readlines()
        
            with open("TrabajoFinal/Trabajo_final_TPI/MVC/Archivos/clientes.txt", "w") as archivo:
                for linea in lineas:
                    if nombre_cliente.lower() not in linea.lower():
                        archivo.write(linea)
            
            archivo.write(f"{nueva_info_cliente['nombre']},{nueva_info_cliente['telefono']},{nueva_info_cliente['email']},{nueva_info_cliente['direccion']},{nueva_info_cliente['cantidad']},{','.join(nueva_info_cliente['lista_nombreMascota'])},{','.join(nueva_info_cliente['lista_tipoMascota'])}\n")
        
        
            self.cargarDatosClientes()
        
        else:
            print(f"No se encontró ningún cliente con el nombre '{nombre_cliente}'")

        
        
#endregion

#region Controlador Mascota
    def mostrarMascotas(self):
        lista_aux = []
        for mascota in self.lista_mascotas:
            if mascota.mascotaActiva():
                lista_aux.append(mascota)
            self.vista.mostrarTodasMascotas(lista_aux)


    def agregarMascota(self):
        tipo,raza = self.vista.IngresoTipoyRaza()
        if self.verificarAgregarTipoyRaza(tipo,raza):
            tipoAnimal = tipo
            nombreRaza = raza
            identificador, propietario, nombreAnimal, detalleMascota, stateMascota = self.vista.agregarMascotaOpciones()
            cadena =f"{tipoAnimal},{nombreRaza},{identificador},{propietario},{nombreAnimal},{detalleMascota},{stateMascota}"
            linea = cadena + "\n"
            self.lista_mascotas.append(Mascota(tipoAnimal, nombreRaza,identificador,propietario,nombreAnimal,detalleMascota,stateMascota))
            with open("Archivos/mascotas.txt", "a", encoding="UTF-8") as file:
                file.write(linea)
                self.vista.mensajeMascotaAgregadaconExito(linea)
        else:
            self.vista.mensajeFaltaDato()


    def verificarAgregarTipoyRaza(self,tipo,raza):
        for animal in self.lista_razas:
            if animal.tipoAnimal == tipo and animal.nombreRaza == raza:
                return True
        return False


    def modificarMascota(self):
        propietario, nombreAnimal = self.vista.mascotaAModificar()
        mascota_encontrada = None

        for mascota in self.lista_mascotas:
            if mascota.propietario == propietario and mascota.nombreAnimal == nombreAnimal:
                mascota_encontrada = mascota
                break

        if mascota_encontrada:
            self.vista.mostrarDatoActualMascota(mascota_encontrada)
            nuevo_identificador, nuevo_nombreAnimal, nuevo_detalleMascota, nuevo_stateMascota = self.vista.modificarDatosMascotas(
                mascota_encontrada)
            mascota_encontrada.set_identificador(nuevo_identificador)
            mascota_encontrada.set_nombreAnimal(nuevo_nombreAnimal)
            mascota_encontrada.set_historial(nuevo_detalleMascota)
            mascota_encontrada.set_stateMascota(nuevo_stateMascota)

            with open("Archivos/mascotas.txt", "w", encoding="UTF-8") as file:
                for mascota in self.lista_mascotas:
                    linea = f"{mascota.tipoAnimalRaza},{mascota.nombreRazaAnimal},{mascota.identificador},{mascota.propietario},{mascota.nombreAnimal},{mascota.detalleMascota},{mascota.stateMascota}\n"
                    file.write(linea)

            self.vista.mascotaCargaExitosa()
        else:
            self.vista.mascotaCargaFallida()


    def buscarMascota(self):
        propietario, nombreAnimal=self.vista.mascotaAModificar()
        for mascota in self.lista_mascotas:
            if mascota.propietario == propietario and mascota.nombreAnimal == nombreAnimal:
                self.vista.mostrarMascotaBuscada(mascota)



    #endregion


#region Raza Menu
    def mostrarRazas(self):
        lista_aux = []
        for raza in self.lista_razas:
            if raza.razaActiva():
                lista_aux.append(raza)
        self.vista.mostrarTodasRazas(lista_aux)

    def agregarRaza(self):
        tipo, raza = self.vista.IngresoTipoyRaza()
        if not self.verificarAgregarTipoyRaza(tipo, raza):
            tipoAnimal = tipo
            nombreRaza = raza
            tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,esperanzaVidaRaza, state = self.vista.agregarRazaOpciones()
            cadena = f"{tipoAnimal},{nombreRaza},{tamanoRaza},{personalidadRaza},{pelajeRaza},{cuidadosRaza},{energiaRaza},{esperanzaVidaRaza},{state}"
            linea = cadena + "\n"
            self.lista_razas.append(
                Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,esperanzaVidaRaza,state))
            with open("Archivos/raza.txt", "a", encoding="UTF-8") as file:
                file.write(linea)
                self.vista.mensajeRazaAgregadaconExito(linea)
        else:
            self.vista.mensajeRazaFallida()


    def modificarRaza(self):
        tipoAnimal, nombreRaza = self.vista.razaAModificar()
        raza_encontrada = None


        for raza in self.lista_razas:
            if raza.tipoAnimal == tipoAnimal and raza.nombreRaza == nombreRaza:
                raza_encontrada = raza
                break

        if raza_encontrada:
            self.vista.mostrarDatoActualRaza(raza_encontrada)
            nuevo_tamanoRaza, nuevo_personalidadRaza, nuevo_pelajeRaza, nuevo_cuidadosRaza, nuevo_energiaRaza,nuevo_esperanzaVidaRaza, nuevo_state = self.vista.modificarDatosRaza(raza_encontrada)

            raza_encontrada.set_tamanoRaza(nuevo_tamanoRaza)
            raza_encontrada.set_personalidadRaza(nuevo_personalidadRaza)
            raza_encontrada.set_pelajeRaza(nuevo_pelajeRaza)
            raza_encontrada.set_cuidadosRaza(nuevo_cuidadosRaza)
            raza_encontrada.set_energiaRaza(nuevo_energiaRaza)
            raza_encontrada.set_esperanzaVidaRaza(nuevo_esperanzaVidaRaza)
            raza_encontrada.set_state(nuevo_state)

            with open("Archivos/raza.txt", "w", encoding="UTF-8") as file:
                for raza in self.lista_razas:
                    linea = f"{raza.tipoAnimal},{raza.nombreRaza},{raza.tamanoRaza},{raza.personalidadRaza},{raza.pelajeRaza},{raza.cuidadosRaza},{raza.energiaRaza},{raza.esperanzaVidaRaza},{raza.state}\n"
                    file.write(linea)

            self.vista.mascotaCargaExitosa()
        else:
            self.vista.razaCargaFallida()


    def eliminarRaza(self):
        tipoAnimal, nombreRaza = self.vista.razaAModificar()
        raza_encontrada = None
        for raza in self.lista_razas:
            if raza.tipoAnimal == tipoAnimal and raza.nombreRaza == nombreRaza:
                raza_encontrada = raza
                break
        if raza_encontrada:
            self.vista.mostrarDatoActualRaza(raza_encontrada)
            nuevo_state=self.vista.eliminarDatosRaza(raza_encontrada)
            raza_encontrada.set_state(nuevo_state)

            with open("Archivos/raza.txt", "w", encoding="UTF-8") as file:
                for raza in self.lista_razas:
                    linea = f"{raza.tipoAnimal},{raza.nombreRaza},{raza.tamanoRaza},{raza.personalidadRaza},{raza.pelajeRaza},{raza.cuidadosRaza},{raza.energiaRaza},{raza.esperanzaVidaRaza},{raza.state}\n"
                    file.write(linea)
        else:
            self.vista.razaCargaFallida()

    #endregion


    def Inicializador(self):
        # Carga de archivos...
        self.cargaDatosClientes()
        self.cargaDatosVeterinarios()
        self.cargaDatosMascotas()
        self.cargaDatosRaza()
        self.cargaDatosDiagnostico()
        self.cargarDatosTratamientos()
        self.cargaDatosVacunas()
        
        # Menú principal...
        while True:
            opcion = self.vista.principalMenu()
            if opcion == 1:
                while True:
                    sub_opcion = self.vista.historialMenu()
                    
                    if sub_opcion == 1:
                        nombreCliente, nombreMascota = self.vista.consultarHistorial()
                        self.consulta_Historial(nombreCliente, nombreMascota)
                    elif sub_opcion == 2:
                        self.vista.modificarHistorial()
                    elif sub_opcion == 3:
                        self.vista.eliminarhistorial()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 2:
                while True:
                    sub_opcion = self.vista.clientesMenu()
                    
                    if sub_opcion == 1:
                        self.informacion_cliente()
                    
                    elif sub_opcion == 2:
                        while True:
                            self.agregar_nuevo_cliente()
                            eleccion = self.vista.mensajeRepeticion()
                            if eleccion == 9:
                                break
                    
                    elif sub_opcion == 3:
                        self.modificar_informacion_Cliente()
                        
                    
                    elif sub_opcion == 4:
                        self.vista.eliminarCliente()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 3:
                while True:
                    sub_opcion = self.vista.veterinariosMenu()
                    if sub_opcion == 1:
                        self.vista.consultarListaVeterinarios()
                    elif sub_opcion == 2:
                        self.vista.agregarNuevoVeterinario()
                    elif sub_opcion == 3:
                        self.vista.modificarEstadoVeterinario()
                    elif sub_opcion == 4:
                        self.vista.eliminarVeterinario()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 4:
                while True:
                    sub_opcion = self.vista.animalesMenu()
                    if sub_opcion == 1:
                        self.mostrarMascotas()
                    elif sub_opcion == 2:
                        self.agregarMascota()
                    elif sub_opcion == 3:
                        self.modificarMascota()
                    elif sub_opcion == 4:
                        self.buscarMascota()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 5:
                while True:
                    sub_opcion = self.vista.razasMenu()
                    if sub_opcion == 1:
                        self.mostrarRazas()
                    elif sub_opcion == 2:
                        self.agregarRaza()
                    elif sub_opcion == 3:
                        self.modificarRaza()
                    elif sub_opcion == 4:
                        self.eliminarRaza()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 6:
                while True:
                    sub_opcion = self.vista.diagnosticoMenu()
                    if sub_opcion == 1:
                        self.vista.consultarDiagnostico()
                    elif sub_opcion == 2:
                        self.vista.agregarDiagnostico()
                    elif sub_opcion == 3:
                        self.vista.modificarDiagnostico()
                    elif sub_opcion == 4:
                        self.vista.eliminarDiagnostico()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 7:
                while True:
                    sub_opcion = self.vista.tratamientoMenu()
                    if sub_opcion == 1:
                        self.vista.consultarTratamiento()
                    elif sub_opcion == 2:
                        self.vista.agregarTratamiento()
                    elif sub_opcion == 3:
                        self.vista.modificarTratamiento()
                    elif sub_opcion == 4:
                        self.vista.eliminarTratamiento()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 8:
                while True:
                    sub_opcion = self.vista.vacunasMenu()
                    if sub_opcion == 1:
                        self.vista.consultarVacunas()
                    elif sub_opcion == 2:
                        self.vista.agregarVacunas()
                    elif sub_opcion == 3:
                        self.vista.modificarVacunas()
                    elif sub_opcion == 4:
                        self.vista.eliminarVacunas()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break
            
            
            elif opcion == 9:
                break






