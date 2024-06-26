    # region Imports
import os
from pathlib import Path
from collections import Counter, defaultdict

from MVC.Modelo.Cliente import Cliente
from MVC.Modelo.Verinario import Veterinario
from MVC.Modelo.Mascota import Mascota
from MVC.Modelo.Raza import Raza
from MVC.Modelo.Diagnostico import Diagnostico
from MVC.Modelo.Tratamiento import Tratamiento
from MVC.Modelo.Vacuna import Vacuna
from MVC.Vista.vista import Vista

# endregion

class Controller:
    
    #region Constructor
    def __init__(self):
        self.lista_clientes = []
        self.lista_veterinarios = []
        self.lista_mascotas = []
        self.lista_razas = []
        self.lista_diagnostico = []
        self.lista_tratamiento = []
        self.lista_vacuna = []
        self.ruta_fichas_medicas = Path("Archivos/Fichas Medicas")
        self.vista = Vista()
        
    #endregion

    #region Parametro de clases
    def menuParametros(self):
        cliente = Cliente()
        veterinario = Veterinario()

        mascota = Mascota()
        raza = Raza()

        diagnostico = Diagnostico()
        tratamiento = Tratamiento()
        vacuna = Vacuna()

        return cliente,veterinario,mascota,raza,diagnostico,tratamiento,vacuna
    
    def limpiar_consola(self):
        try:
            os.system("cls")
        except:
            os.system("clear")

    #endregion

    # region Carga de Archivos

    def cargarDatosClientes(self):
        try:
            with open("Archivos/clientes.txt", "r", encoding="UTF-8") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                partes = linea.strip().split(";")
                if len(partes) != 7:
                    raise ValueError(f"Línea con formato incorrecto: {linea}")

                nombre, telefono, email, direccion, cantidad = partes[:5]
                cantidad = int(cantidad)

                # Convertir las listas desde las cadenas
                nombreMascota = partes[5].strip("[]").split(", ")
                tipoMascotas = partes[6].strip("[]").split(", ")

                # Quitar comillas simples de los elementos de las listas
                nombreMascota = [item.strip("'") for item in nombreMascota]
                tipoMascotas = [item.strip("'") for item in tipoMascotas]

                cliente = Cliente(nombre, telefono, email, direccion, cantidad, nombreMascota, tipoMascotas)
                self.lista_clientes.append(cliente)
            self.vista.cargaExitosa("clientes")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de clientes: {str(e)}")

    def actualizarArchivoClientes(self):
        with open("Archivos/clientes.txt", "w", encoding="UTF-8") as archivo:
            for cliente in self.lista_clientes:
                nombres_mascotas = ",".join(cliente.getNombreMascotas()) if isinstance(cliente.getNombreMascotas(),
                                                                                       list) else cliente.getNombreMascotas()
                tipos_mascotas = ",".join(cliente.getTipoMascota()) if isinstance(cliente.getTipoMascota(),
                                                                                  list) else cliente.getTipoMascota()
                linea_cliente = f"{cliente.nombre};{cliente.telefono};{cliente.email};{cliente.direccion};{cliente.cantidad};[{nombres_mascotas}];[{tipos_mascotas}]"
                archivo.write(f"{linea_cliente}\n")

    def cargaDatosVeterinarios(self):
        try:
            with open("Archivos/veterinarios.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombre, telefono, cargo, estado = datos
                veterinario = Veterinario(nombre,telefono,cargo,estado)
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
                mascota = Mascota(tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal,
                                  detalleMascota, stateMascota)
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
                raza = Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,
                            esperanzaVidaRaza, int(state))
                self.lista_razas.append(raza)
            self.vista.cargaExitosa("raza")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de raza: {str(e)}")

    def cargaDatosDiagnostico(self):
        try:
            with open("Archivos/Diagnosticos.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombreDiag, descripcionDiag, cuidadosDiag, state = datos
                diagnostico = Diagnostico(nombreDiag, descripcionDiag, cuidadosDiag)
                self.lista_diagnostico.append(diagnostico)
            self.vista.cargaExitosa("diagnostico")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de diagnóstico: {str(e)}")

    def cargarDatosTratamientos(self):
        try:
            with open("Archivos/tratamientos.txt", "r") as archivo:
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
            with open("Archivos/Vacunas.txt", "r") as archivo:
                lineas = archivo.readlines()
            for linea in lineas:
                datos = linea.strip().split(",")
                nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis, state = datos
                vacuna = Vacuna(nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis, state)
                self.lista_vacuna.append(vacuna)
            self.vista.cargaExitosa("vacunas")
        except Exception as e:
            self.vista.mensajeError(f"Error cargando datos de vacunas: {str(e)}")

    # endregion



    #region Controlador Clientes
    def informacion_cliente(self):
        self.vista.consultarLista(self.lista_clientes)

    def agregar_nuevo_cliente(self):
        nombre, telefono, email, direccion, cantidad, lista_nombreMascota, lista_tipoMascota = self.vista.agregarNuevocliente()
        if any(cliente.nombre == nombre for cliente in self.lista_clientes):
            self.vista.mensajeError("El cliente ya existe.")
        else:
            cliente = Cliente(nombre, telefono, email, direccion, cantidad, lista_nombreMascota, lista_tipoMascota)
            linea_cliente = f"{nombre};{telefono};{email};{direccion};{cantidad};{lista_nombreMascota};{lista_tipoMascota}"
            self.lista_clientes.append(cliente)
            with open("Archivos/clientes.txt", "a") as archivo:
                archivo.write(f"{linea_cliente}\n")
            self.vista.cargaExitosa("cliente")


            for i in range(cantidad):
                tipo = lista_tipoMascota[i]
                raza = self.vista.IngresoRaza(tipo)
                identificador = self.vista.IngresoIdentificador(nombre, lista_nombreMascota[i])
                propietario = nombre
                nombreAnimal = lista_nombreMascota[i]
                detalleMascota = self.vista.IngresoDetalleMascota(nombreAnimal)
                stateMascota = 1
                cadena_mascota = f"{tipo},{raza},{identificador},{propietario},{nombreAnimal},{detalleMascota},{stateMascota}"
                linea_mascota = cadena_mascota + "\n"
                self.lista_mascotas.append(
                    Mascota(tipo, raza, identificador, propietario, nombreAnimal, detalleMascota, stateMascota))
                with open("Archivos/mascotas.txt", "a", encoding="UTF-8") as file:
                    file.write(linea_mascota)
                self.vista.mensajeMascotaAgregadaconExito(linea_mascota)
            
   
    def modificar_informacion_Cliente(self):
        nombre_cliente = input("Ingrese el nombre del cliente que desea modificar: ")
    
        cliente_encontrado = None
        for cliente in self.lista_clientes:
            if cliente.nombre.lower() == nombre_cliente.lower():
                cliente_encontrado = cliente
                break
    
        if cliente_encontrado:
            cliente.nombre,nuevo_telefono,nuevo_email,nueva_direccion,cantidad_mascotas,nueva_lista_nombre_mascotas,nueva_lista_tipo_mascotas = self.vista.modificarInformacionCliente(cliente_encontrado)
            cliente.telefono = nuevo_telefono
            cliente.email = nuevo_email
            cliente.direccion = nueva_direccion
            cliente.cantidad = cantidad_mascotas
            cliente.nombreMascota = nueva_lista_nombre_mascotas
            cliente.tipoMascotas = nueva_lista_tipo_mascotas
        
        
            with open("Archivos/clientes.txt", "w") as archivo:
                for client in self.lista_clientes:
                    archivo.write(str(client))
        
        else:
            print(f"No se encontró ningún cliente con el nombre '{nombre_cliente}'")

    def eliminarCliente(self):
        nombre_cliente = input("Ingrese el nombre del cliente que desea eliminar: ")
        for cliente in self.lista_clientes:
            if cliente.nombre.lower() == nombre_cliente.lower():
                self.lista_clientes.remove(cliente)
            else:
                pass

        with open("MVC/Archivos/clientes.txt", "w") as archivo:
                for client in self.lista_clientes:
                    archivo.write(str(client))
        
    #endregion

    # region Controlador Mascota
    def mostrarMascotas(self):
        lista_aux = []
        for mascota in self.lista_mascotas:
            if mascota.mascotaActiva():
                lista_aux.append(mascota)
        self.vista.mostrarTodasMascotas(lista_aux)

    def agregarMascota(self):
        tipo, raza = self.vista.IngresoTipoyRaza()
        if self.verificarAgregarTipoyRaza(tipo, raza):
            propietario = self.vista.IngresoPropietario()
            cliente_existe = False
            for cliente in self.lista_clientes:
                if cliente.nombre == propietario:
                    cliente_existe = True
                    break

            if not cliente_existe:
                self.vista.mostrarMensaje("El cliente no existe. Agregue el cliente primero.")
                return

            tipoAnimal = tipo
            nombreRaza = raza
            identificador, nombreAnimal, detalleMascota, stateMascota = self.vista.agregarMascotaOpciones(propietario)
            cadena = f"{tipoAnimal},{nombreRaza},{identificador},{propietario},{nombreAnimal},{detalleMascota},{stateMascota}"
            linea = cadena + "\n"

            # Agregar la mascota a la lista de mascotas
            self.lista_mascotas.append(
                Mascota(tipoAnimal, nombreRaza, identificador, propietario, nombreAnimal, detalleMascota, stateMascota))
            with open("Archivos/mascotas.txt", "a", encoding="UTF-8") as file:
                file.write(linea)
                self.vista.mensajeMascotaAgregadaconExito(linea)

            # Actualizar la información del cliente en la lista
            for cliente in self.lista_clientes:
                if cliente.nombre == propietario:
                    cliente.cantidad = int(cliente.cantidad) + 1
                    # Usar métodos existentes para agregar nombres y tipos de mascotas
                    cliente.agregarNombreMascota(nombreAnimal)
                    cliente.agregarTipoMascota(tipoAnimal)

                    # Actualizar el archivo de clientes
                    self.actualizarArchivoClientes()
                    break
        else:
            self.vista.mensajeFaltaDato()




    def verificarAgregarTipoyRaza(self, tipo, raza):
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
        propietario, nombreAnimal = self.vista.mascotaAModificar()
        for mascota in self.lista_mascotas:
            if mascota.propietario == propietario and mascota.nombreAnimal == nombreAnimal:
                self.vista.mostrarMascotaBuscada(mascota)

    def buscarMascotaValidada(self):
        propietario, nombreAnimal = self.vista.mascotaAModificar()
        for mascota in self.lista_mascotas:
            if mascota.propietario == propietario and mascota.nombreAnimal == nombreAnimal and mascota.mascotaActiva():
                self.vista.mostrarMascotaBuscada(mascota)
                return True,propietario,nombreAnimal
        return False,None,None


    def buscarMascotaValidada2(self,propietario,nombreAnimal):
        for mascota in self.lista_mascotas:
            if mascota.propietario == propietario and mascota.nombreAnimal == nombreAnimal and mascota.mascotaActiva():
                self.vista.mostrarMascotaBuscada(mascota)
                return True
        return False

    def mascotaPropietarioValidador3(self, propietario, nombreAnimal):
        cliente_existe = False
        mascota_existe = False
        for cliente in self.lista_clientes:
            if cliente.nombre == propietario:
                cliente_existe = True
                nombreMascotas = cliente.getNombreMascotas()
                if nombreAnimal in nombreMascotas:
                    mascota_existe = True
                    self.vista.mostrarMascotaBuscada2(nombreAnimal, propietario)
                    break
        return cliente_existe, mascota_existe

    # endregion

    # region Vacuna Menu

    def mostrarVacunas(self):
        lista_aux_vacuna = []
        for vacuna in self.lista_vacuna:
            if vacuna.state == 1:
                lista_aux_vacuna.append(vacuna)
        self.vista.mostrarTodasVacunas(lista_aux_vacuna)

    def agregarVacuna(self):
        nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis, state = self.vista.agregarVacunaOpciones()
        cadena = f"{nombreVacuna},{loteVacuna},{numeroDosis},{diasProximaDosis},{state}"
        linea = cadena + "\n"
        self.lista_vacuna.append(
            Vacuna(nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis, state)
        )
        vacuna = Vacuna(Vacuna(nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis, state))
        with open("Archivos/vacunas.txt", "a", encoding="UTF-8") as file:
            file.write(linea)
        self.vista.mensajeVacunaAgregadaconExito(linea)
        return vacuna







    def modificarVacuna(self):
        nombreVacuna = self.vista.vacunaAModificar()
        vacuna_encontrada = None

        for vacuna in self.lista_vacuna:
            if vacuna.nombreVacuna == nombreVacuna:
                vacuna_encontrada = vacuna
                break

        if vacuna_encontrada:
            self.vista.mostrarDatoActualVacuna(vacuna_encontrada)
            nuevo_nombreVacuna, nuevo_loteVacuna, nuevo_numeroDosis, nuevo_diasProximaDosis, nuevo_state = self.vista.modificarDatosVacuna(
                vacuna_encontrada)
            vacuna_encontrada.setNombreVacuna(nuevo_nombreVacuna)
            vacuna_encontrada.setLoteVacuna(nuevo_loteVacuna)
            vacuna_encontrada.setNumeroDosis(nuevo_numeroDosis)
            vacuna_encontrada.setdiasProximaDosis = nuevo_diasProximaDosis
            vacuna_encontrada.setstate(nuevo_state)

            print(self.lista_vacuna)

            with open("Archivos/vacunas.txt", "w", encoding="UTF-8") as file:
                for vacuna in self.lista_vacuna:
                    linea = f"{vacuna.nombreVacuna},{vacuna.loteVacuna},{vacuna.numeroDosis},{vacuna.diasProximaDosis},{vacuna.state}\n"
                    file.write(linea)
            self.vista.vacunaCargaExitosa()
        else:
            self.vista.vacunaCargaFallida()

    def eliminarVacuna(self):
        nombreVacuna = self.vista.vacunaAEliminar()
        vacuna_encontrada = None

        for vacuna in self.lista_vacuna:
            if vacuna.nombreVacuna == nombreVacuna:
                vacuna_encontrada = vacuna
                break

        if vacuna_encontrada:
            self.vista.mostrarDatoActualVacuna(vacuna_encontrada)
            nuevo_state = self.vista.eliminarDatosVacuna(vacuna_encontrada)
            vacuna_encontrada.setstate(nuevo_state)

            with open("Archivos/vacunas.txt", "w", encoding="UTF-8") as file:
                for vacuna in self.lista_vacuna:
                    linea = f"{vacuna.nombreVacuna},{vacuna.loteVacuna},{vacuna.numeroDosis},{vacuna.diasProximaDosis},{vacuna.state}\n"
                    file.write(linea)

            self.vista.vacunaEliminadaConExito()
        else:
            self.vista.vacunaNoEncontrada()

    # endregion

    # region Raza Menu
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
            tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, state = self.vista.agregarRazaOpciones()
            cadena = f"{tipoAnimal},{nombreRaza},{tamanoRaza},{personalidadRaza},{pelajeRaza},{cuidadosRaza},{energiaRaza},{esperanzaVidaRaza},{state}"
            linea = cadena + "\n"
            self.lista_razas.append(
                Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,
                     esperanzaVidaRaza, state))
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
            nuevo_tamanoRaza, nuevo_personalidadRaza, nuevo_pelajeRaza, nuevo_cuidadosRaza, nuevo_energiaRaza, nuevo_esperanzaVidaRaza, nuevo_state = self.vista.modificarDatosRaza(
                raza_encontrada)

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
            nuevo_state = self.vista.eliminarDatosRaza(raza_encontrada)
            raza_encontrada.set_state(nuevo_state)

            with open("Archivos/raza.txt", "w", encoding="UTF-8") as file:
                for raza in self.lista_razas:
                    linea = f"{raza.tipoAnimal},{raza.nombreRaza},{raza.tamanoRaza},{raza.personalidadRaza},{raza.pelajeRaza},{raza.cuidadosRaza},{raza.energiaRaza},{raza.esperanzaVidaRaza},{raza.state}\n"
                    file.write(linea)
        else:
            self.vista.razaCargaFallida()

    # endregion

    # region Tratamiento Menu

    def mostrarTratamientos(self):
        lista_aux = []
        for tratamiento in self.lista_tratamiento:
            if tratamiento.tratamientoActivo():
                lista_aux.append(tratamiento)
        self.vista.mostrarTratamientosPantalla(lista_aux)

    def agregarTratamiento(self):
        nombreTratamiento, duracionTratamiento, state = self.vista.agregarTratamientoOpciones()
        cadena = f"{nombreTratamiento},{duracionTratamiento},{state}"
        linea = cadena + "\n"
        self.lista_tratamiento.append(
            Tratamiento(nombreTratamiento, duracionTratamiento, state)
        )
        with open("Archivos/tratamientos.txt", "a", encoding="UTF-8") as file:
            file.write(linea)
        print(self.lista_tratamiento)
        self.vista.tratamientoCargaExitosa()

    def agregarTratamiento2(self):
        nombreTratamiento, duracionTratamiento, state = self.vista.agregarTratamientoOpciones()
        tratamiento = Tratamiento(nombreTratamiento, duracionTratamiento, state)
        self.lista_tratamiento.append(tratamiento)

        with open("Archivos/tratamientos.txt", "a", encoding="UTF-8") as file:
            file.write(f"{nombreTratamiento},{duracionTratamiento},{state}\n")

        self.vista.tratamientoCargaExitosa()
        return tratamiento


    def modificarTratamiento(self):
        nombreTratamiento = self.vista.tratamientoAModificar()
        tratamiento_encontrado = None

        for tratamiento in self.lista_tratamiento:
            if tratamiento.nombreTratamiento == nombreTratamiento:
                tratamiento_encontrado = tratamiento
                break

        if tratamiento_encontrado:
            self.vista.mostrarDatoActualTratamiento(tratamiento_encontrado)
            nuevo_nombreTratamiento, nueva_duracionTratamiento, nuevo_state = self.vista.modificarDatosTratamiento(
                tratamiento_encontrado)
            tratamiento_encontrado.setNombretratamiento(nuevo_nombreTratamiento)
            tratamiento_encontrado.setDuracionTratamiento(nueva_duracionTratamiento)
            tratamiento_encontrado.setState(nuevo_state)

            with open("Archivos/tratamientos.txt", "w", encoding="UTF-8") as file:
                for tratamiento in self.lista_tratamiento:
                    linea = f"{tratamiento.nombreTratamiento},{tratamiento.duracionTratamiento},{tratamiento.state}\n"
                    file.write(linea)

            self.vista.tratamientoCargaExitosa()
        else:
            self.vista.tratamientoCargaFallida()

    def eliminarTratamiento(self):
        nombreTratamiento = self.vista.tratamientoAEliminar()
        tratamiento_encontrado = None

        for tratamiento in self.lista_tratamiento:
            if tratamiento.nombreTratamiento == nombreTratamiento:
                tratamiento_encontrado = tratamiento
                break

        if tratamiento_encontrado:
            self.vista.mostrarDatoActualTratamiento(tratamiento_encontrado)
            nuevo_state = self.vista.eliminarDatosTratamiento(tratamiento_encontrado)
            tratamiento_encontrado.setState(nuevo_state)

            with open("Archivos/tratamientos.txt", "w", encoding="UTF-8") as file:
                for tratamiento in self.lista_tratamiento:
                    linea = f"{tratamiento.nombreTratamiento},{tratamiento.duracionTratamiento},{tratamiento.state}\n"
                    file.write(linea)

            self.vista.tratamientoEliminadoConExito()
        else:
            self.vista.tratamientoNoEncontrado()

    # endregion

    #region Diagnostico
    def consultar_Diagnostico(self):
        self.limpiar_consola()
        self.vista.consultarLista(self.lista_diagnostico)
    def agregar_Diagnostico(self):
        self.limpiar_consola()
        nombreDiag,descripcionDiag,cuidadosDiag,state = self.vista.agregarDiagnostico()

        if any(diagnostico.nombreDiag == nombreDiag for diagnostico in self.lista_diagnostico):
            self.vista.mensajeError("El Diagnostico ya existe.")
        else:
            diagnostico = Diagnostico(nombreDiag, descripcionDiag, cuidadosDiag, state)
            self.lista_diagnostico.append(diagnostico)
            with open("Archivos/Diagnosticos.txt", "a") as archivo:
                archivo.write(f"{diagnostico}\n")
            self.vista.cargaExitosa("diagnostico")
            return diagnostico

    def modificar_Diagnostico(self):
        pass
    def eliminar_Diagnostico(self):
        pass
#endregion

    #region CONSULTA


    def generarNuevaConsulta(self,propietario,nombreMascota):
        continuar= self.buscarMascotaValidada2(propietario,nombreMascota)
        if not continuar:
            return

        lista_del_dia = []
        fecha = self.vista.fechaHoy()

        veterinario = self.atencionVeterinario()
        if not veterinario:
            opcion = self.vista.agregarNuevoOpcion("veterinario")
            if opcion == "y":
                nuevo_veterinario = self.agregar_Nuevo_Veterinario()
                veterinario = nuevo_veterinario
            elif opcion == "n":
                return


        diagnostico = self.diagosticoNombre()
        if not diagnostico:
            opcion = self.vista.agregarNuevoOpcion("diagnóstico")
            if opcion == "y":
                nuevo_diagnostico = self.agregar_Diagnostico()
                diagnostico = nuevo_diagnostico
            elif opcion == "n":
                return

        tratamiento = self.tratamientoNombre()
        if not tratamiento:
            opcion = self.vista.agregarNuevoOpcion("tratamiento")
            if opcion == "y":
                nuevo_tratamiento = self.agregarTratamiento2()
                tratamiento = nuevo_tratamiento
                print(tratamiento)
            elif opcion == "n":
                return

        vacuna = self.vacunaNombre()
        if not vacuna:
            opcion = self.vista.agregarNuevoOpcion("vacuna")
            if opcion == "y":
                nuevo_vacuna = self.agregarVacuna()
                vacuna = nuevo_vacuna
            elif opcion == "n":
                return

        observaciones = self.observaciones()

        lista_del_dia.append(
            (fecha, veterinario.nombre, diagnostico.getNombreDiag(),tratamiento.getNombreTratamiento(), vacuna.nombreVacuna,
             observaciones)
        )
        return lista_del_dia

    def atencionVeterinario(self):
        nombre_veterinario = self.vista.veterinarioNombre()
        for veterinario in self.lista_veterinarios:
            if veterinario.nombre == nombre_veterinario:
                return veterinario
        self.vista.mostrarMensaje(f"No existe veterinario con el nombre {nombre_veterinario}")
        return None

    def diagosticoNombre(self):
        diagnosticoNombreBuscado = self.vista.DiagnosticoNombre()
        for diagnostico in self.lista_diagnostico:
            if diagnostico.nombreDiag == diagnosticoNombreBuscado:
                self.vista.mensajeDiagnosticoEncontrado()
                return diagnostico

        self.vista.mostrarMensaje(f"No existe diagnóstico con el nombre {diagnosticoNombreBuscado}")
        return None

    def diagosticoNombre(self):
        diagnosticoNombreBuscado = self.vista.DiagnosticoNombre()
        for diagnostico in self.lista_diagnostico:
            if diagnostico.nombreDiag == diagnosticoNombreBuscado:
                self.vista.mensajeDiagnosticoEncontrado()
                return diagnostico

        self.vista.mostrarMensaje(f"No existe diagnóstico con el nombre {diagnosticoNombreBuscado}")
        return None

    def tratamientoNombre(self):
        tratamientoNombreBuscado = self.vista.TratamientoNombre()
        for tratamiento in self.lista_tratamiento:
            if tratamiento.nombreTratamiento == tratamientoNombreBuscado:
                self.vista.mensajeTratamientoEncontrado()
                return tratamiento
        self.vista.mostrarMensaje(f"No existe tratamiento con el nombre {tratamientoNombreBuscado}")
        return None

    def vacunaNombre(self):
        vacunaNombreBuscado = self.vista.VacunaNombre()
        for vacuna in self.lista_vacuna:
            if vacuna.nombreVacuna == vacunaNombreBuscado:
                return vacuna

        self.vista.mostrarMensaje(f"No existe vacuna con el nombre {vacunaNombreBuscado}")
        return None

    def observaciones(self):
        observacion_ingreso = self.vista.IngresoObservacion()
        return observacion_ingreso

    #endregion

    #region FichaMedica

    def manejarFichasMedicas(self):
        propietario, nombreMascota = self.vista.ingresopropietarioYMascota()


        cliente_existe, mascota_existe = self.mascotaPropietarioValidador3(propietario, nombreMascota)
        if not cliente_existe:
            self.vista.mostrarMensaje("No se encontró el cliente. Volviendo al menú anterior.")
            return
        if cliente_existe and not mascota_existe:
            self.vista.mostrarMensaje("Cliente existe, Mascota no existe! Agregue la mascota.")
            return

        ficha_existe, ruta_ficha = self.buscarFichaMedica(propietario, nombreMascota)
        if ficha_existe:
            lista_del_dia = self.generarNuevaConsulta(propietario, nombreMascota)
            if lista_del_dia:
                self.agregarConsultaAFicha(ruta_ficha, lista_del_dia)
        else:
            self.vista.mostrarMensaje("No se encontró la ficha médica.")
            crear_archivo = input("¿Desea crear una nueva ficha médica? [s/n]: ").lower()
            if crear_archivo == 's':
                cliente_existe, mascota_existe = self.mascotaPropietarioValidador3(propietario, nombreMascota)
                if not mascota_existe:
                    self.vista.mostrarMensaje("Mascota no ENCONTRADA! Cargar Mascota ")
                    return

                ruta_ficha.touch()
                self.crearEncabezadoFichaMedica(ruta_ficha, propietario, nombreMascota)
                lista_del_dia = self.generarNuevaConsulta(propietario, nombreMascota)
                if lista_del_dia:
                    self.agregarConsultaAFicha(ruta_ficha, lista_del_dia)
            else:
                self.vista.mostrarMensaje("Operación cancelada. Volviendo al menú anterior.")
                return

    def agregarConsultaAFicha(self, ruta_ficha, lista_del_dia):
        with open(ruta_ficha, "a") as archivo:
            for item in lista_del_dia:
                archivo.write(";".join(item) + "\n")
        print("Consulta registrada exitosamente.")


    def buscarFichaMedica(self, propietario, nombreMascota):
        archivo_ficha = f"{nombreMascota}_{propietario}.txt"
        ruta_archivo = self.ruta_fichas_medicas / archivo_ficha
        return ruta_archivo.exists(), ruta_archivo

    def buscarUnaFicha(self):
        propietario = input("Ingrese el nombre del propietario: ")
        nombreMascota = input("Ingrese el nombre de la mascota: ")

        ficha_existe, ruta_ficha = self.buscarFichaMedica(propietario, nombreMascota)
        if ficha_existe:
            self.mostrarContenidoFicha(ruta_ficha)
        else:
            self.vista.mostrarMensaje("No se encontró la ficha médica. Volviendo al menú anterior.")
            return

    def mostrarContenidoFicha(self, ruta_ficha):
        with open(ruta_ficha, "r", encoding="UTF-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            self.vista.mostrarMensaje("La ficha médica está vacía.")
            return


        encabezado = lineas[0].strip().split(",")
        tipo_mascota, raza, nombre_mascota, nombre_propietario = encabezado
        self.vista.mostrarEncabezadoFicha(tipo_mascota, raza, nombre_mascota, nombre_propietario)

        consultas = []
        for linea in lineas[1:]:
            consulta = linea.strip().split(";")
            fecha, medico, diagnostico, tratamiento, vacuna, *observacion = consulta
            observacion = observacion[0] if observacion else "N/A"
            consultas.append((fecha, medico, diagnostico, tratamiento, vacuna, observacion))

        self.vista.mostrarConsultasFicha(consultas)

    def crearEncabezadoFichaMedica(self, ruta_ficha, propietario, nombreMascota):

        cliente = next((cliente for cliente in self.lista_clientes if cliente.nombre == propietario), None)
        mascota = next((mascota for mascota in self.lista_mascotas if
                        mascota.propietario == propietario and mascota.nombreAnimal == nombreMascota), None)

        if cliente and mascota:
            tipo = mascota.tipoAnimalRaza
            raza = mascota.nombreRazaAnimal
            identificador = mascota.identificador


            encabezado = f"{tipo},{raza},{nombreMascota},{propietario}\n"

            with open(ruta_ficha, "w", encoding="UTF-8") as archivo:
                archivo.write(encabezado)
        else:
            self.vista.mostrarMensaje(
                "Error al crear el encabezado de la ficha médica. No se encontró el cliente o la mascota.")

    #endregion

    #region Veterinario
    def consultar_Lista_Veterinarios(self):
        try:
            self.vista.consultarLista(self.lista_veterinarios)
        except:
            self.vista.mensajeError("no hay lista de veterinarios cargada.")
    def agregar_Nuevo_Veterinario(self):
        nombre, telefono, cargo, estado = self.vista.agregarNuevoVeterinario()
        veterinario = Veterinario(nombre, telefono, cargo, estado)
        self.lista_veterinarios.append(veterinario)
        return veterinario

        with open("Archivos/veterinarios.txt", "a") as archivo:
            archivo.write(f"{nombre},{telefono},{cargo},{estado}\n")
        self.vista.cargaExitosa("veterinario")

    def modificar_Estado_Veterinario(self):
        nombre = self.vista.modificarEstadoVeterinario()
        encontrado = False
        for veterinario in self.lista_veterinarios:
            if nombre == veterinario['nombre']:
                estado = veterinario['estado']
                opcion = self.vista.pedirOpcionModificar(estado)
                if opcion == '1':
                    nuevoEstado = 'inactivo' if estado == 'activo' else 'activo'
                    veterinario['estado'] = nuevoEstado
                    self.vista.mostrarMensaje(f"El veterinario {nombre} ahora está {nuevoEstado}.")
                    self.guardarVeterinarios()
                    encontrado = True
                break
            if not encontrado:
                self.vista.mostrarMensaje(f"No se encontró al veterinario con nombre {nombre}.")

        with open('veterinarios.txt', 'w') as file:
            for veterinario in self.lista_veterinarios:
                linea = f"{veterinario['nombre']},{veterinario['telefono']},{veterinario['cargo']},{veterinario['estado']}\n"
                file.write(linea)


        self.vista.modificarEstadoVeterinario(False)

    def eliminar_Veterinario(self):
        nombre = self.vista.eliminarVeterinario()
        encontrado = False
        for veterinario in self.lista_veterinarios:
            if nombre == veterinario:
                self.lista_veterinarios.remove(veterinario)
                encontrado = True
                break

        if encontrado:
            self.vista.mostrarMensaje(f"El veterinario {nombre} ha sido eliminado.")
            self.guardarVeterinarios()
        else:
            self.vista.mostrarMensaje(f"No se encontró al veterinario con nombre {nombre}.")

    def guardarVeterinarios(self):
        with open('Archivos/veterinarios.txt', 'w') as file:
            for veterinario in self.lista_veterinarios:
                linea = f"{veterinario['nombre']},{veterinario['telefono']},{veterinario['cargo']},{veterinario['estado']}\n"
                file.write(linea)

#endregion

    #region Menu Controlador
    def Inicializador(self):
        # Carga de archivos...
        self.cargarDatosClientes()
        self.cargaDatosVeterinarios()
        self.cargaDatosMascotas()
        self.cargaDatosRaza()
        self.cargaDatosDiagnostico()
        self.cargarDatosTratamientos()
        self.cargaDatosVacunas()
        self.limpiar_consola()

        # Menú principal...
        while True:
            opcion = self.vista.principalMenu()



            if opcion == 0:
                while True:
                    sub_opcion = self.vista.estadisticasMenu()
                    if sub_opcion == 1:
                        self.mostrarEncabezadoYConsultas()
                    elif sub_opcion == 2:
                        self.buscarUnaFicha()
                    elif sub_opcion == 3:
                        self.rankingDiagnosticos()
                    elif sub_opcion == 4:
                        self.diagnosticosPorRaza()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break


            elif opcion == 1:
                while True:
                    sub_opcion = self.vista.historialMenu()

                    if sub_opcion == 1:
                        self.manejarFichasMedicas()
                    elif sub_opcion == 2:
                        self.buscarUnaFicha()
                    elif sub_opcion == 3:
                        self.agregar_nuevo_cliente()
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
                        self.consultar_Lista_Veterinarios()
                    elif sub_opcion == 2:
                        self.agregar_Nuevo_Veterinario()
                    elif sub_opcion == 3:
                        self.modificar_Estado_Veterinario()
                    elif sub_opcion == 4:
                        self.eliminar_Veterinario()
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
                self.limpiar_consola()
                while True:
                    sub_opcion = self.vista.diagnosticoMenu()
                    if sub_opcion == 1:
                        self.limpiar_consola()
                        self.consultar_Diagnostico()
                    elif sub_opcion == 2:
                        self.limpiar_consola()
                        self.agregar_Diagnostico()
                    elif sub_opcion == 3:
                        self.limpiar_consola()
                        self.modificar_Diagnostico()
                    elif sub_opcion == 4:
                        self.limpiar_consola()
                        self.vista.eliminarDiagnostico()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break

            elif opcion == 7:
                while True:
                    sub_opcion = self.vista.tratamientoMenu()
                    if sub_opcion == 1:
                        self.mostrarTratamientos()
                    elif sub_opcion == 2:
                        self.agregarTratamiento()
                    elif sub_opcion == 3:
                        self.modificarTratamiento()
                    elif sub_opcion == 4:
                        self.eliminarTratamiento()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break

            elif opcion == 8:
                while True:
                    sub_opcion = self.vista.vacunasMenu()
                    if sub_opcion == 1:
                        self.mostrarVacunas()
                    elif sub_opcion == 2:
                        self.agregarVacuna()
                    elif sub_opcion == 3:
                        self.modificarVacuna()
                    elif sub_opcion == 4:
                        self.eliminarVacuna()
                    elif sub_opcion == 9:
                        self.vista.mensajeVolviendoAlMenu()
                        break

            elif opcion == 9:
                break
    #endregion

#region Estadisticas
    def mostrarEncabezadoYConsultas(self):
        propietario = input("Ingrese el nombre del propietario: ")
        nombreMascota = input("Ingrese el nombre de la mascota: ")

        ficha_existe, ruta_ficha = self.buscarFichaMedica(propietario, nombreMascota)
        if ficha_existe:
            self.mostrarContenidoEncabezadoYConsultas(ruta_ficha)
        else:
            self.vista.mostrarMensaje("No se encontró la ficha médica. Volviendo al menú anterior.")
            return

    def mostrarContenidoEncabezadoYConsultas(self, ruta_ficha):
        with open(ruta_ficha, "r", encoding="UTF-8") as archivo:
            lineas = archivo.readlines()

        if not lineas:
            self.vista.mostrarMensaje("La ficha médica está vacía.")
            return


        encabezado = lineas[0].strip().split(",")
        tipo_mascota, raza, nombre_mascota, nombre_propietario = encabezado
        self.vista.mostrarEncabezadoFicha(tipo_mascota, raza, nombre_mascota, nombre_propietario)


        cantidad_consultas = len(lineas) - 1
        self.vista.mostrarCantidadConsultasConSeparador(cantidad_consultas)

    def rankingDiagnosticos(self):
        diagnostico_counter = Counter()

        for ficha_path in self.ruta_fichas_medicas.glob("*.txt"):
            with ficha_path.open("r", encoding="UTF-8") as archivo:
                lineas = archivo.readlines()
                if len(lineas) <= 1:
                    continue

                for linea in lineas[1:]:
                    consulta = linea.strip().split(";")
                    diagnostico = consulta[2]
                    if any(diagnostico == diag.getNombreDiag() for diag in self.lista_diagnostico):
                        diagnostico_counter[diagnostico] += 1

        ranking = diagnostico_counter.most_common()
        self.vista.mostrarRankingDiagnosticos(ranking)


    def diagnosticosPorRaza(self):
        diagnosticos_razas = defaultdict(set)

        for ficha_path in self.ruta_fichas_medicas.glob("*.txt"):
            with ficha_path.open("r", encoding="UTF-8") as archivo:
                lineas = archivo.readlines()
                if len(lineas) <= 1:
                    continue

                encabezado = lineas[0].strip().split(",")
                raza = encabezado[1]

                for linea in lineas[1:]:
                    consulta = linea.strip().split(";")
                    diagnostico = consulta[2]
                    if any(diagnostico == diag.getNombreDiag() for diag in self.lista_diagnostico):
                        diagnosticos_razas[diagnostico].add(raza)

        self.vista.mostrarDiagnosticosPorRaza(diagnosticos_razas)



    #endregion