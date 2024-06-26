class Vista:

    #region Mensajes Extras
    def cargaExitosa(self, tipo_dato):
        print(f"Datos de {tipo_dato} cargados exitosamente.")

    def mensajeError(self, mensaje):
        print(f"Error: {mensaje}")

    def mensajeVolviendoAlMenu(self):
        print("Volviendo al menú principal...")

    def mensajeRepeticion(self):
        print("¿Deseas agregar otro cliente? ([1] - SI [9] salir")
        eleccion = input("Elección: ")
        return int(eleccion)

    def consultarLista(self, lista):
        for elemento in lista:
            print(elemento)

    #endregion

    # region Principal Menu
    def principalMenu(self):
        print("Menú Principal")
        print("1. Historial")
        print("2. Clientes")
        print("3. Veterinarios")
        print("4. Mascotas")
        print("5. Razas")
        print("6. Diagnósticos")
        print("7. Tratamientos")
        print("8. Vacunas")
        print("9. Salir")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    # endregion

    #region Historal Menu
    def historialMenu(self):
        print("Menú de Historial")
        print("1. Consultar Historial")
        print("2. Modificar Historial")
        print("3. Eliminar Historial")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def listaHistoriales(self,cliente, mascota, diagnosticoMascota, tratamientoMascota, vacunas):
        self.nombreCliente = cliente
        self.nombremascota = mascota
        self.diagnosticoMascota = diagnosticoMascota
        self.tratamientoMascota = tratamientoMascota
        self.vacunas = Vacunas
        self.proximaConsulta = str(input("Indique proxima consulta: "))



        return historial

    def consultarHistorial(self):
        nombreCliente = input("Nombre del Cliente: ")
        nombreMascota = input("Nombre de la Mascota: ")
        return nombreCliente, nombreMascota

    def modificarHistorial(self):
        print("Funcionalidad de modificar historial no implementada aún.")

    def eliminarhistorial(self):
        print("Funcionalidad de eliminar historial no implementada aún.")

    #endregion

    #region Cliente Menu
    
    def clientesMenu(self):
        print("Menú de Clientes")
        print("1. Consultar Información de Clientes")
        print("2. Agregar Nuevo Cliente")
        print("3. Modificar Información de Cliente")
        print("4. Eliminar Cliente")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def agregarNuevocliente(self):
        
        print("Agregar Nuevo Cliente")
        self.lista_nombreMascota = []
        self.lista_tipoMascota = []
        
        nombre = str(input("Nombre: "))
        telefono = str(input("Teléfono: "))
        email = str(input("Email: "))
        direccion = str(input("Dirección: "))
        cantidad = int(input("Cantidad de Mascotas: "))
        for c in range(cantidad):
            nombreMascota = input("Nombre de la Mascota: ")
            tipoMascotas = input("Tipo de Mascotas: ")
            self.lista_nombreMascota.append(nombreMascota)
            self.lista_tipoMascota.append(tipoMascotas)
        return nombre,telefono,email,direccion,cantidad,self.lista_nombreMascota,self.lista_tipoMascota
    
    def informacionCliente(self, lista):
            print("Información de Clientes")
            if lista:
                for cliente in lista:
                    print(cliente)
                    print("\n")
            else:
                print("No hay clientes para mostrar")
        
            
    def modificarInformacionCliente(self, cliente):
        print(f"Modificación de Información del Cliente: {cliente.nombre}")
        nuevo_telefono = input(f"Nuevo teléfono ({cliente.telefono}): ").strip() or cliente.telefono
        nuevo_email = input(f"Nuevo email ({cliente.email}): ").strip() or cliente.email
        nueva_direccion = input(f"Nueva dirección ({cliente.direccion}): ").strip() or cliente.direccion
    
    
        print("Mascotas Actuales:")
        for i, mascota in enumerate(cliente.nombreMascota):
            print(f"{i+1}. {mascota} ({cliente.tipoMascotas[i]})")
    
    
        nueva_lista_nombre_mascotas = []
        nueva_lista_tipo_mascotas = []
        cantidad_mascotas = int(input(f"Ingrese la cantidad de mascotas que tiene {cliente.nombre}: "))
    
        for i in range(cantidad_mascotas):
            nombre_mascota = input(f"Nombre de la mascota {i+1}: ").strip()
            tipo_mascota = input(f"Tipo de mascota {i+1} (perro, gato, etc.): ").strip()
            nueva_lista_nombre_mascotas.append(nombre_mascota)
            nueva_lista_tipo_mascotas.append(tipo_mascota)
        
    
        return cliente.nombre,nuevo_telefono,nuevo_email,nueva_direccion,cantidad_mascotas,nueva_lista_nombre_mascotas,nueva_lista_tipo_mascotas
    
    def eliminarCliente(self):
        print("Funcionalidad de eliminar cliente no implementada aún.")
        
#endregion

    #region Veterinario Menu

    def veterinariosMenu(self):
        print("Menú de Veterinarios")
        print("1. Consultar Lista de Veterinarios")
        print("2. Agregar Nuevo Veterinario")
        print("3. Modificar Estado de Veterinario")
        print("4. Eliminar Veterinario")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def consultarListaVeterinarios(self):
        print("Funcionalidad de consultar lista de veterinarios no implementada aún.")

    def agregarNuevoVeterinario(self):
        nombre = input("Nombre del veterinario: ")
        telefono = input("Telefono del veterinario: ")
        cargo = input("Cargo del veterinario: ")
        estado = True
        return nombre, telefono, cargo, estado

        def modificarEstadoVeterinario(self):
            return input("Ingrese el nombre del veterinario que desea conocer el estado: ")

        def mostrarMensaje(self, mensaje):
            print(mensaje)

        def pedirOpcionModificar(self, estado):
            print(f"El estado del veterinario es {estado}. ¿Desea Modificarlo?")
            print("[1] - SI / [2] - NO")
            opcion = input("Ingrese opción: ")
            if opcion == '1':
                if estado:
                    estado = False
                else:
                    estado = True
            return estado

    def eliminarVeterinario(self):
        return input("Ingrese el nombre del veterinario que desea eliminar: ")

    def mostrarMensaje(self, mensaje):
        print(mensaje)

    # endregion

    # region Mascota Menu
    def animalesMenu(self):
        print("Menú de Animales")
        print("1. Consultar Todas las Mascotas")
        print("2. Ingresar Nueva Mascota")
        print("3. Modificar Mascota ")
        print("4. Buscar Mascota ")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def mostrarTodasMascotas(self, lista):
        for mascota in lista:
            print(
                f"Tipo de Animal: {mascota.tipoAnimalRaza}, Raza: {mascota.nombreRazaAnimal},ID: {mascota.identificador},"
                f"Propietario: {mascota.propietario},Nombre Mascota: {mascota.nombreAnimal}, Detalles: {mascota.detalleMascota}")

    def agregarMascotaOpciones(self):
        identificador = input("Ingrese Identificador ").lower()
        propietario = str(input("Ingrese Nombre Propietario ")).lower()
        nombreAnimal = input("Ingrese Nombre Mascota ").lower()
        detalleMascota = input("Ingrese Detalles Mascota ").lower()
        stateMascota = 1
        return identificador, propietario, nombreAnimal, detalleMascota, stateMascota

    def mensajeMascotaAgregadaconExito(self, linea):
        print(f"{linea} Mascota Agregada con Exito! ")

    def IngresoTipoyRaza(self):
        tipo = str(input("Ingrese tipo de Animal ")).lower()
        raza = str(input("Ingrese nombre de Raza ")).lower()
        return tipo, raza

    def mensajeFaltaDato(self):
        print("Falta la Raza, debe agregarla antes! ")

    def mascotaAModificar(self):
        propietario = input("Nombre del Propietario: ").lower()
        nombreAnimal = input("Nombre de la Mascota: ").lower()
        return propietario, nombreAnimal

    def mostrarMascotaBuscada(self, mascota):
        if mascota.mascotaActiva():
            print(mascota)
        elif mascota.stateMascota == 0:
            print("Mascota Inactiva o Borrada")

    def mostrarDatoActualMascota(self, mascota):
        print(mascota)

    def mascotaCargaExitosa(self):
        print("Mascota cargada con éxito!")

    def mascotaCargaFallida(self):
        print("Mascota no encontrada, carga fallida!")

    def mascotaAModificar(self):
        propietario = input("Nombre del Propietario: ").lower()
        nombreAnimal = input("Nombre de la Mascota: ").lower()
        return propietario, nombreAnimal

    def mostrarDatoActualMascota(self, mascota):
        print(mascota)

    def modificarDatosMascotas(self, mascota):
        print("Modificar datos de la Mascota")
        print("Dejar en blanco para conservar original")
        identificador = input(f"nuevo identificador ({mascota.identificador}): ") or mascota.identificador
        nombreAnimal = input(f"nuevo nombre mascota ({mascota.nombreAnimal}): ") or mascota.nombreAnimal
        detalleMascota = input(f"nuevo Detalle mascota ({mascota.detalleMascota}): ") or mascota.detalleMascota
        stateMascota = input(f"1 activo // 0 inactivo-eliminar ({mascota.stateMascota}): ") or mascota.stateMascota
        return identificador, nombreAnimal, detalleMascota, int(stateMascota)

    # endregion

    # region Raza Menu

    def razasMenu(self):
        print("Menú de Razas")
        print("1. Consultar Razas disponibles")
        print("2. Agregar Nueva Raza")
        print("3. Modificar Raza")
        print("4. Eliminar Raza")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def mostrarTodasRazas(self, lista_aux):
        for raza in lista_aux:
            print(f"Tipo Animal: {raza.tipoAnimal}, Nombre Raza: {raza.nombreRaza}, Tamaño Raza:{raza.tamanoRaza}, "
                  f"Personalidad Raza:{raza.personalidadRaza}, Pelaje Raza: {raza.pelajeRaza}, Cuidados Raza:{raza.cuidadosRaza} ")

    def mensajeRazaAgregadaconExito(self, linea):
        print(f"{linea} Raza Agregada con Exito! ")

    def mensajeRazaFallida(self):
        print("Carga Fallida, La Raza ya se encuentra en la lista de razas")

    def razaAModificar(self):
        tipoAnimal = input("Tipo Animal: ").lower()
        nombreRaza = input("Nombre de la Raza: ").lower()
        return tipoAnimal, nombreRaza

    def mostrarDatoActualRaza(self, raza):
        print(raza)

    def modificarDatosRaza(self, raza):
        print("Modificar datos de la Raza")
        print("Dejar en blanco para conservar original")

        tamanoRaza = input(f"nuevo tamaño raza ({raza.tamanoRaza}): ") or raza.tamanoRaza
        personalidadRaza = input(f"nueva personalidad raza ({raza.personalidadRaza}): ") or raza.personalidadRaza
        pelajeRaza = input(f"nuevo pelaje raza ({raza.pelajeRaza}): ") or raza.pelajeRaza
        cuidadosRaza = input(f"nuevos cuidados raza ({raza.cuidadosRaza}): ") or raza.cuidadosRaza
        energiaRaza = input(f"nueva energía raza ({raza.energiaRaza}): ") or raza.energiaRaza
        esperanzaVidaRaza = input(
            f"nueva esperanza de vida raza ({raza.esperanzaVidaRaza}): ") or raza.esperanzaVidaRaza
        state = input(f"1 activo // 0 inactivo-eliminar ({raza.state}): ") or raza.state

        return tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, int(state)

    def agregarRazaOpciones(self):
        tamanoRaza = input("Ingrese Tamaño de la Raza ").lower()
        personalidadRaza = input("Ingrese Personalidad de la Raza ").lower()
        pelajeRaza = input("Ingrese Tipo de Pelaje de la Raza ").lower()
        cuidadosRaza = input("Ingrese Cuidados Necesarios para la Raza ").lower()
        energiaRaza = input("Ingrese Nivel de Energía de la Raza ").lower()
        esperanzaVidaRaza = input("Ingrese Esperanza de Vida de la Raza ").lower()
        state = 1  # Asumiendo que el estado por defecto es activo

        return tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, state

    def razaCargaFallida(self):
        print("Raza no encontrada, carga fallida!")

    def eliminarDatosRaza(self, raza):
        print("Eliminando Raza...")
        print(raza)
        state = int(0)
        return state

    def razaCargaExitosa(self):
        print("Raza cargada con éxito!")

    # endregion

    #region Diagnostico Menu

    def diagnosticoMenu(self):
        print("Menú de Diagnósticos")
        print("1. Consultar Diagnóstico")
        print("2. Agregar Nuevo Diagnóstico")
        print("3. Modificar Diagnóstico")
        print("4. Eliminar Diagnóstico")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

        # region Diagnostico Menu

    def diagnosticoMenu(self):
        print("Menú de Diagnósticos")
        print("1. Consultar Diagnóstico")
        print("2. Agregar Nuevo Diagnóstico")
        print("3. Modificar Diagnóstico")
        print("4. Eliminar Diagnóstico")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def consultarDiagnostico(self, lista):
        print("Funcionalidad de consultar diagnóstico no implementada aún.")
        if lista:
            print("Diagnosticos Cargados")
            for diagnostico in lista:
                print(diagnostico.nombreDiag)
                print("\n")
        else:
            print("No hay diagnosticos para mostrar")

    def agregarDiagnostico(self):
        nombreDiag = input("Nombre del diagnostico: ")
        descripcionDiag = input("Descripcion del diagnostico")
        cuidadosDiag = input("Cuidados del diagnostico")
        return nombreDiag, descripcionDiag, cuidadosDiag, True

    def modificarDiagnostico(self):
        print("Funcionalidad de modificar diagnóstico no implementada aún.")

    # endregion

    #region Tratamiento Menu

    def tratamientoMenu(self):
        print("Menú de Tratamientos")
        print("1. Consultar Tratamiento")
        print("2. Agregar Nuevo Tratamiento")
        print("3. Modificar Tratamiento")
        print("4. Eliminar Tratamiento")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def mostrarTratamientosPantalla(self, lista):
        for elemento in lista:
            print(elemento)

    def agregarTratamientoOpciones(self):
        nombreTratamiento = input("Ingrese Nombre del Tratamiento: ").lower()
        duracionTratamiento = input("Ingrese Duración del Tratamiento: ").lower()
        state = int(input("Ingrese Estado del Tratamiento (1 para activo, 0 para inactivo): "))
        return nombreTratamiento, duracionTratamiento, state

    def tratamientoAModificar(self):
        nombreTratamiento = input("Nombre del Tratamiento a modificar: ").lower()
        return nombreTratamiento

    def mostrarDatoActualTratamiento(self, tratamiento):
        print(f"Nombre Tratamiento: {tratamiento.nombreTratamiento}, Duración: {tratamiento.duracionTratamiento}, Estado: {tratamiento.state} ")

    def modificarDatosTratamiento(self, tratamiento):
        print("Modificar datos del Tratamiento")
        print("Dejar en blanco para conservar original")
        nombreTratamiento = input(
            f"nuevo nombre tratamiento ({tratamiento.nombreTratamiento}): ") or tratamiento.nombreTratamiento
        duracionTratamiento = input(
            f"nueva duración del tratamiento ({tratamiento.duracionTratamiento}): ") or tratamiento.duracionTratamiento
        state = int(input(f"1 activo // 0 inactivo ({tratamiento.state}): ") or tratamiento.state)
        return nombreTratamiento, duracionTratamiento, state

    def eliminarDatosTratamiento(self, tratamiento):
        print("Eliminando Tratamiento...")
        print(tratamiento)
        state = int(0)
        return state

    def tratamientoAEliminar(self):
        nombreTratamiento = input("Nombre del tratamiento a eliminar: ").lower()
        return nombreTratamiento

    def tratamientoEliminadoConExito(self):
        print("Tratamiento eliminado con éxito (estado cambiado a inactivo)!")

    def tratamientoNoEncontrado(self):
        print("Tratamiento no encontrado, eliminación fallida!")

    def tratamientoCargaExitosa(self):
        print("Tratamiento cargado con éxito!")

    def tratamientoCargaFallida(self):
        print("Tratamiento no encontrado, carga fallida!")

#endregion

    # region Vacuna Menu

    def vacunasMenu(self):
        print("Menú de Vacunas")
        print("1. Consultar Vacunas")
        print("2. Agregar Nueva Vacuna")
        print("3. Modificar Vacuna")
        print("4. Eliminar Vacuna")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def mostrarTodasVacunas(self, lista):
        for vacuna in lista:
            print(
                f"Nombre de la Vacuna: {vacuna.nombreVacuna}, Lote: {vacuna.loteVacuna}, Número de Dosis: {vacuna.numeroDosis}, "
                f"Días para Próxima Dosis: {vacuna.proximaDosis}")

    def agregarVacunaOpciones(self):
        nombreVacuna = input("Ingrese Nombre de la Vacuna: ").lower()
        loteVacuna = input("Ingrese Lote de la Vacuna: ").lower()
        numeroDosis = input("Ingrese Número de Dosis: ").lower()
        diasProximaDosis = input("Ingrese Días para la Próxima Dosis: ").lower()
        state = 1
        return nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis, state

    def vacunaAModificar(self):
        nombreVacuna = input("Nombre de la Vacuna a modificar: ").lower()
        return nombreVacuna

    def mostrarDatoActualVacuna(self, vacuna):
        print(
            f"Nombre Vacuna: {vacuna.nombreVacuna}, Lote: {vacuna.loteVacuna}, Número de Dosis: {vacuna.numeroDosis}, Próxima Dosis: {vacuna.proximaDosis}, Estado: {vacuna.state}")

    def modificarDatosVacuna(self, vacuna):
        print("Modificar datos de la Vacuna")
        nombreVacuna = input(f"nuevo nombre vacuna ({vacuna.nombreVacuna}): ") or vacuna.nombreVacuna
        loteVacuna = input(f"nuevo lote vacuna ({vacuna.loteVacuna}): ") or vacuna.loteVacuna
        numeroDosis_input = input(f"nuevo número de dosis ({vacuna.numeroDosis}): ")
        numeroDosis = int(numeroDosis_input) if numeroDosis_input else vacuna.numeroDosis
        #diasProximaDosis = int(input(f" días para próxima dosis: ")) or vacuna.diasProximaDosis
        diasProximaDosis_input = input(f"días para próxima dosis ({vacuna.diasProximaDosis}): ")
        diasProximaDosis = int(diasProximaDosis_input) if diasProximaDosis_input else vacuna.diasProximaDosis
        state = int(input(f"1 activo // 0 inactivo ({vacuna.state}): ") or vacuna.state)
        return nombreVacuna, loteVacuna, numeroDosis, diasProximaDosis, state

    def vacunaCargaExitosa(self):
        print("Vacuna cargada con éxito!")

    def vacunaCargaFallida(self):
        print("Vacuna no encontrada, carga fallida!")

    def mensajeVacunaAgregadaconExito(self, linea):
        print(f"Vacuna agregada con exito: {linea}")

    def vacunaAEliminar(self):
        nombreVacuna = input("Nombre de la Vacuna a eliminar: ").lower()
        return nombreVacuna

    def eliminarDatosVacuna(self, vacuna):
        print("Eliminando Vacuna...")
        print(vacuna)
        state = int(0)
        return state

    def vacunaEliminadaConExito(self):
        print("Vacuna eliminada con éxito (estado cambiado a inactivo)!")

    def vacunaNoEncontrada(self):
        print("Vacuna no encontrada, eliminación fallida!")

    # endregion

    #region Consulta
    def fechaHoy(self):
        fecha= input("Ingrese Fecha ")
        return fecha

    def veterinarioNombre(self):
        veterinario_nombre=input("Ingrese Nombre Veterinario ")
        return veterinario_nombre

    def MensajeVeterinarioInexistente(self):
        print("No existe ese veterinario, debe cargarlo ")

    def DiagnosticoNombre(self):
        nombre_diagnostico = input("Ingrese Nombre Diagnostico ")
        return nombre_diagnostico

    def TratamientoNombre(self):
        return input("Ingrese el nombre del tratamiento: ")

    def mensajeDiagnosticoEncontrado(self):
        print("Diagnistico Encontrado ")

    def MensajeDiagnisticoInexistente(self):
        print("Diangnostico inexistente cargar Diagnostico ")

    def mensajeTratamientoEncontrado(self):
        print("Diangnostico inexistente cargar Diagnostico ")

    def VacunaNombre(self):
        vacuna_nombre = input("Nombre Vacuna")
        return vacuna_nombre

    def IngresoObservacion(self):
        observacion = input("Ingrese observacion ")
        return observacion

    def mostrarMensaje(self, mensaje):
        print(mensaje)

    #endregion