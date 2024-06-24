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
    
#endregion
    
#region Principal Menu
    def principalMenu(self):
        print("Menú Principal")
        print("1. Historial")
        print("2. Clientes")
        print("3. Veterinarios")
        print("4. Animales")
        print("5. Razas")
        print("6. Diagnósticos")
        print("7. Tratamientos")
        print("8. Vacunas")
        print("9. Salir")
        opcion = input("Selecciona una opción: ")
        return int(opcion)
#endregion

#region Historal Menu
    def historialMenu(self):
        print("Menú de Historial")
        print("1. Consultar Historial")
        print("2. Modificar Historial")
        print("3. Eliminar Historial")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)
    
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
        return {
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "direccion": direccion,
            "cantidad": cantidad,
            "nombreMascota": self.lista_nombreMascota,
            "tipoMascotas": self.lista_tipoMascota
        }
    
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
        for i, mascota in enumerate(cliente.lista_nombreMascota):
            print(f"{i+1}. {mascota} ({cliente.lista_tipoMascota[i]})")
    
    
        nueva_lista_nombre_mascotas = []
        nueva_lista_tipo_mascotas = []
        cantidad_mascotas = int(input(f"Ingrese la cantidad de mascotas que tiene {cliente.nombre}: "))
    
        for i in range(cantidad_mascotas):
            nombre_mascota = input(f"Nombre de la mascota {i+1}: ").strip()
            tipo_mascota = input(f"Tipo de mascota {i+1} (perro, gato, etc.): ").strip()
            nueva_lista_nombre_mascotas.append(nombre_mascota)
            nueva_lista_tipo_mascotas.append(tipo_mascota)
    
        nueva_info_cliente = {
            'nombre': cliente.nombre,
            'telefono': nuevo_telefono,
            'email': nuevo_email,
            'direccion': nueva_direccion,
            'cantidad': cantidad_mascotas,
            'lista_nombreMascota': nueva_lista_nombre_mascotas,
            'lista_tipoMascota': nueva_lista_tipo_mascotas
        }
    
        return nueva_info_cliente
    
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
        print("Funcionalidad de agregar nuevo veterinario no implementada aún.")
    
    def modificarEstadoVeterinario(self):
        print("Funcionalidad de modificar estado de veterinario no implementada aún.")
    
    def eliminarVeterinario(self):
        print("Funcionalidad de eliminar veterinario no implementada aún.")

#endregion

#region Animales Menu
    def animalesMenu(self):
        print("Menú de Animales")
        print("1. Consultar Animales Internados")
        print("2. Ingresar Nuevo Animal")
        print("3. Modificar Estado de Animal")
        print("4. Reegreso de Animal")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)
    
    def animalesInternados(self):
        print("Funcionalidad de consultar animales internados no implementada aún.")
    
    def ingresoAnimal(self):
        print("Funcionalidad de ingreso de animal no implementada aún.")
    
    def modificarEstadoAnimal(self):
        print("Funcionalidad de modificar estado de animal no implementada aún.")
    
    def reegresoAnimal(self):
        print("Funcionalidad de reegreso de animal no implementada aún.")
        
#endregion

#region Raza Menu
    
    def razasMenu(self):
        print("Menú de Razas")
        print("1. Consultar Raza de Animal")
        print("2. Agregar Nueva Raza")
        print("3. Modificar Raza")
        print("4. Eliminar Raza")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)
    
    def consultarRazaAnimal(self):
        print("Funcionalidad de consultar raza de animal no implementada aún.")
    
    def agregarRaza(self):
        print("Funcionalidad de agregar raza no implementada aún.")
    
    def modificarRaza(self):
        print("Funcionalidad de modificar raza no implementada aún.")
    
    def eliminarRaza(self):
        print("Funcionalidad de eliminar raza no implementada aún.")
#endregion

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
    
    def consultarDiagnostico(self):
        print("Funcionalidad de consultar diagnóstico no implementada aún.")
    
    def agregarDiagnostico(self):
        print("Funcionalidad de agregar diagnóstico no implementada aún.")
    
    def modificarDiagnostico(self):
        print("Funcionalidad de modificar diagnóstico no implementada aún.")
    
    def eliminarDiagnostico(self):
        print("Funcionalidad de eliminar diagnóstico no implementada aún.")
        
#endregion

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
    
    def consultarTratamiento(self):
        print("Funcionalidad de consultar tratamiento no implementada aún.")
    
    def agregarTratamiento(self):
        print("Funcionalidad de agregar tratamiento no implementada aún.")
    
    def modificarTratamiento(self):
        print("Funcionalidad de modificar tratamiento no implementada aún.")
    
    def eliminarTratamiento(self):
        print("Funcionalidad de eliminar tratamiento no implementada aún.")

#endregion

#region Vacunas Menu
    
    def vacunasMenu(self):
        print("Menú de Vacunas")
        print("1. Consultar Vacunas")
        print("2. Agregar Nueva Vacuna")
        print("3. Modificar Vacuna")
        print("4. Eliminar Vacuna")
        print("9. Volver al Menú Principal")
        opcion = input("Selecciona una opción: ")
        return int(opcion)

    def consultarVacunas(self):
        print("Funcionalidad de consultar vacunas no implementada aún.")
    
    def agregarVacunas(self):
        print("Funcionalidad de agregar vacunas no implementada aún.")
    
    def modificarVacunas(self):
        print("Funcionalidad de modificar vacunas no implementada aún.")
    
    def eliminarVacunas(self):
        print("Funcionalidad de eliminar vacunas no implementada aún.")

#endregion
