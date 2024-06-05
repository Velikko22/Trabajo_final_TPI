from Trabajo_final_TPI.Clases.Mascota import Mascota
from Trabajo_final_TPI.Clases.Raza import Raza

from pathlib import Path
lista_razas_objetos = []
lista_mascota_objetos = []
RUTA_RAZAS = Path('Datos archivos.txt//listas de razas')
RUTA_MASCOTAS = Path('Datos archivos.txt//listas de mascotas')

#Busquedas
def buscarRaza(tipo, raza):
    archivo_a_buscar = f"{tipo}_{raza}.txt"
    archivo_path = RUTA_RAZAS / archivo_a_buscar
    if archivo_path.exists():
        print("Raza encontrada...")
        return True
    else:
        print("RAZA NO ENCONTRADA")
        return False

#Agregar
def agregarMascota(tipo, raza):
    continuar_carga = buscarRaza(tipo, raza)
    if continuar_carga:
        identificador = input("Ingrese ID mascota: ").lower()
        propietario = input("Ingrese nombre propietario: ").lower()
        nombreAnimal = input("Ingrese nombre del animal: ").lower()
        historial = input("Ingrese historial: ").lower()
        stateMascota = input("Ingrese estado de la mascota: ").lower()

        linea = f"{tipo};{raza};{identificador};{propietario};{nombreAnimal};{historial};{stateMascota}"
        nombre_archivo = f"{identificador}_{propietario}.txt"
        lugar_y_nombre_archivo = RUTA_MASCOTAS / nombre_archivo

        with lugar_y_nombre_archivo.open("w", encoding="UTF-8") as file:
            file.write(linea)
            print("Archivo creado y guardado.")
        file.flush()


def agregarRaza(tipo,raza):
    no_continuar_carga = buscarRaza(tipo, raza)
    if no_continuar_carga:
        print("Raza ya existente...probar con otra...")
    else:
        tipoAnimal = tipo
        nombreRaza = raza
        tamanoRaza = input("Tamaño de la raza: ").lower()
        personalidadRaza = input("Personalidad de la raza: ").lower()
        pelajeRaza = input("Pelaje de la raza: ").lower()
        cuidadosRaza = input("Cuidados de la raza: ").lower()
        energiaRaza = input("Energía de la raza: ").lower()
        esperanzaVidaRaza = input("Esperanza de vida de la raza: ").lower()
        state = input("Estado de la raza: ").lower()

        linea = f"{tipoAnimal};{nombreRaza};{tamanoRaza};{personalidadRaza};{pelajeRaza};{cuidadosRaza};{energiaRaza};" \
                f"{esperanzaVidaRaza};{state}"

        nombre_archivo = f"{tipo}_{raza}.txt"
        lugar_y_nombre_archivo = RUTA_RAZAS / nombre_archivo

        with lugar_y_nombre_archivo.open("w", encoding="UTF-8") as file:
            file.write(linea)
            file.flush()
        print("Archivo creado y guardado.")


#consultas

def consultarMascota(id_mascota,propietario):
    archivo_a_buscar = f"{id_mascota}_{propietario}.txt"
    archivo_path = RUTA_MASCOTAS/archivo_a_buscar
    if archivo_path.exists():
        with open(archivo_path,"r",encoding="UTF-8") as file:
            archivo = file.readline()
            datos = archivo.split(";")
            tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, historial, stateMascota = datos
        lista_mascota_objetos.append(
            Mascota(tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, historial,
                    stateMascota))
        for objeto in lista_mascota_objetos:
            print(objeto)
        lista_mascota_objetos.clear()
    else:
        print(f"El archivo {archivo_a_buscar} no existe en el directorio {RUTA_MASCOTAS}")


def consultarRaza(tipo,nombre_raza):
    archivo_a_buscar = f"{tipo}_{nombre_raza}.txt"
    archivo_path = RUTA_RAZAS / archivo_a_buscar
    if archivo_path.exists():
        with open(archivo_path, "r", encoding="UTF-8") as file:
            archivo = file.readline()
            datos = archivo.split(";")
            tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, \
            energiaRaza, esperanzaVidaRaza, state = datos
        lista_razas_objetos.append(Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza,
                                          cuidadosRaza, energiaRaza,esperanzaVidaRaza, state ))
        for objeto in lista_razas_objetos:
            print(objeto)
        lista_razas_objetos.clear()
    else:
        print(f"El archivo {archivo_a_buscar} no existe en el directorio {RUTA_MASCOTAS}")

# Consultar Listado total
def consultarRazasCargadas():
    archivos = list(RUTA_RAZAS.glob('*'))
    if archivos:
        print(f"Razas Cargadas")
        for archivo in archivos:
            print(archivo.name)
    else:
        print(f"No se encontraron archivos en el directorio {RUTA_RAZAS}.")



def validarRazasCargadas():
    archivos = list(RUTA_RAZAS.glob('*'))
    if archivos:
        for archivo in archivos:
            print(archivo.name)
    else:
        print(f"No se encontraró la Raza, debe cargarla!")


def consultarMascotasCargadas():
    archivos = list(RUTA_MASCOTAS.glob('*'))
    if archivos:
        print(f"MASCOTAS Cargadas")
        for archivo in archivos:
            print(archivo.name)

    else:
        print(f"No se encontraron archivos en el directorio {RUTA_MASCOTAS}.")


#Modificar

def modificarMascota(id_mascota,propietario):
    archivo_a_buscar = f"{id_mascota}_{propietario}.txt"
    archivo_path = RUTA_MASCOTAS/archivo_a_buscar
    if not archivo_path.exists():
        print("ERROR: EL ARCHIVO NO EXISTE")
        print("REGRESANDO A MENU...")
        return

    if archivo_path.exists():
        with open(archivo_path,"r",encoding="UTF-8") as file:
            archivo = file.readline()
            datos = archivo.split(";")
            tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, historial, stateMascota = datos
        mascota_objeto= (Mascota(tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, historial,
                    stateMascota))
        lista_mascota_objetos.append(mascota_objeto)
        continuar_modificacion = True
        while continuar_modificacion == True:
            try:
                print("===============")
                print("Que desea modificar? ")
                print("1 Tipo Animal\n 2 Nombre Raza \n 3 Identificador Mascota\n 4 Nombre Propietario\n 5 Nombre Mascota\n "
                      "6 historial\n 7 stateMascota\n 0 Salir y Guardar cambios")
                opcion = int(input("?... "))

                if opcion == 1:
                    nuevo_tipo = input("Nuevo tipo: ").lower()
                    mascota_objeto.set_tipoAnimalRaza(nuevo_tipo)
                    print(f"Modificado a {mascota_objeto.get_tipoAnimalRaza()}")
                elif opcion == 2:
                    nuevo_nombre_raza = input("Nuevo nombre de raza: ").lower()
                    mascota_objeto.set_nombreRazaAnimal(nuevo_nombre_raza)
                    print(f"Modificado a {mascota_objeto.get_nombreRazaAnimal()}")
                elif opcion == 3:
                    nuevo_identificador = input("Nuevo identificador: ").lower()
                    mascota_objeto.set_identificador(nuevo_identificador)
                    print(f"Modificado a {mascota_objeto.get_identificador()}")

                elif opcion == 4:
                    nuevo_propietario = input("Nuevo propietario: ").lower()
                    mascota_objeto.set_propietario(nuevo_propietario)
                    print(f"Modificado a {mascota_objeto.get_propietario()}")

                elif opcion == 5:
                    nuevo_nombreAnimal = input("Nuevo identificador: ").lower()
                    mascota_objeto.set_nombreAnimal(nuevo_nombreAnimal)
                    print(f"Modificado a {mascota_objeto.get_nombreAnimal()}")

                elif opcion == 6:
                    nuevo_historial = input("Nuevo historial: ").lower()
                    mascota_objeto.set_historial(nuevo_historial)
                    print(f"Modificado a {mascota_objeto.get_historial()}")
                elif opcion == 7:
                    nuevo_stateMascota = input("Nuevo estado de mascota: ").lower()
                    mascota_objeto.set_stateMascota(nuevo_stateMascota)
                    print(f"Modificado a {mascota_objeto.get_stateMascota()}")


                elif opcion == 0:
                    if buscarRaza(mascota_objeto.get_tipoAnimalRaza(), mascota_objeto.get_nombreRazaAnimal()):
                        # Borrar el archivo existente
                        archivo_path.unlink()

                        # Crear nuevo nombre de archivo
                        nuevo_nombre_archivo = f"{mascota_objeto.get_identificador()}_{mascota_objeto.get_propietario()}.txt"
                        nuevo_archivo_path = RUTA_MASCOTAS / nuevo_nombre_archivo

                        # Guardar los cambios en un nuevo archivo
                        with open(nuevo_archivo_path, "w", encoding="UTF-8") as file:
                            file.write(f"{mascota_objeto.get_tipoAnimalRaza()};{mascota_objeto.get_nombreRazaAnimal()};"
                                       f"{mascota_objeto.get_identificador()};{mascota_objeto.get_propietario()};"
                                       f"{mascota_objeto.get_nombreAnimal()};{mascota_objeto.get_historial()};"
                                       f"{mascota_objeto.get_stateMascota()}")
                        print("Cambios guardados exitosamente.")
                        continuar_modificacion = False
                    else:
                        print("La raza modificada no existe. No se guardaron los cambios. Debe Crearla! ")

            except ValueError:
                print("Por favor, ingrese un número válido.")


def modificarRaza(tipoAnimal, nombreRaza):
    archivo_a_buscar = f"{tipoAnimal}_{nombreRaza}.txt"
    archivo_path = RUTA_RAZAS / archivo_a_buscar
    if not archivo_path.exists():
        print("ERROR: EL ARCHIVO NO EXISTE")
        print("REGRESANDO A MENU...")
        return

    if archivo_path.exists():
        with open(archivo_path, "r", encoding="UTF-8") as file:
            archivo = file.readline()
            datos = archivo.split(";")
            tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, state = datos
        raza_objeto = Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, state)
        lista_razas_objetos.append(raza_objeto)
        continuar_modificacion = True
        while continuar_modificacion:
            try:
                print("===============")
                print("¿Qué desea modificar?")
                print("1 Tipo Animal\n2 Nombre Raza\n3 Tamaño Raza\n4 Personalidad Raza\n5 Pelaje Raza\n6 Cuidados Raza\n7 Energía Raza\n8 Esperanza de Vida Raza\n9 Estado Raza\n0 Salir y Guardar cambios")
                opcion = int(input("?... "))

                if opcion == 1:
                    nuevo_tipo = input("Nuevo tipo: ").lower()
                    raza_objeto.set_tipoAnimal(nuevo_tipo)
                    print(f"Modificado a {raza_objeto.get_tipoAnimal()}")
                elif opcion == 2:
                    nuevo_nombre_raza = input("Nuevo nombre de raza: ").lower()
                    raza_objeto.set_nombreRaza(nuevo_nombre_raza)
                    print(f"Modificado a {raza_objeto.get_nombreRaza()}")
                elif opcion == 3:
                    nuevo_tamano = input("Nuevo tamaño: ").lower()
                    raza_objeto.set_tamanoRaza(nuevo_tamano)
                    print(f"Modificado a {raza_objeto.get_tamanoRaza()}")
                elif opcion == 4:
                    nueva_personalidad = input("Nueva personalidad: ").lower()
                    raza_objeto.set_personalidadRaza(nueva_personalidad)
                    print(f"Modificado a {raza_objeto.get_personalidadRaza()}")
                elif opcion == 5:
                    nuevo_pelaje = input("Nuevo pelaje: ").lower()
                    raza_objeto.set_pelajeRaza(nuevo_pelaje)
                    print(f"Modificado a {raza_objeto.get_pelajeRaza()}")
                elif opcion == 6:
                    nuevos_cuidados = input("Nuevos cuidados: ").lower()
                    raza_objeto.set_cuidadosRaza(nuevos_cuidados)
                    print(f"Modificado a {raza_objeto.get_cuidadosRaza()}")
                elif opcion == 7:
                    nueva_energia = input("Nueva energía: ").lower()
                    raza_objeto.set_energiaRaza(nueva_energia)
                    print(f"Modificado a {raza_objeto.get_energiaRaza()}")
                elif opcion == 8:
                    nueva_esperanza_vida = input("Nueva esperanza de vida: ").lower()
                    raza_objeto.set_esperanzaVidaRaza(nueva_esperanza_vida)
                    print(f"Modificado a {raza_objeto.get_esperanzaVidaRaza()}")
                elif opcion == 9:
                    nuevo_state = input("Nuevo estado: ").lower()
                    raza_objeto.set_state(nuevo_state)
                    print(f"Modificado a {raza_objeto.get_state()}")
                elif opcion == 0:
                    # Borrar el archivo existente
                    archivo_path.unlink()

                    # Crear nuevo nombre de archivo
                    nuevo_nombre_archivo = f"{raza_objeto.get_tipoAnimal()}_{raza_objeto.get_nombreRaza()}.txt"
                    nuevo_archivo_path = RUTA_RAZAS / nuevo_nombre_archivo

                    # Guardar los cambios en un nuevo archivo
                    with open(nuevo_archivo_path, "w", encoding="UTF-8") as file:
                        file.write(f"{raza_objeto.get_tipoAnimal()};{raza_objeto.get_nombreRaza()};"
                                   f"{raza_objeto.get_tamanoRaza()};{raza_objeto.get_personalidadRaza()};"
                                   f"{raza_objeto.get_pelajeRaza()};{raza_objeto.get_cuidadosRaza()};"
                                   f"{raza_objeto.get_energiaRaza()};{raza_objeto.get_esperanzaVidaRaza()};"
                                   f"{raza_objeto.get_state()}")
                    print("Cambios guardados exitosamente.")
                    continuar_modificacion = False

            except ValueError:
                print("Por favor, ingrese un número válido.")











def menu_principal():
    menu_principal_abierto = True
    while menu_principal_abierto:
        print("\nMenú Principal:")
        print("1. Ver/Agregar/Modificar Raza")
        print("2. Ver/Agregar/Modificar Mascotas")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            menu_razas()
        elif opcion == '2':
            menu_mascotas()
        elif opcion == '0':
            print("Saliendo...")
            menu_principal_abierto = False
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_razas():
    menu_razas_abierto = True
    while menu_razas_abierto:
        print("\nMenú Razas:")
        print("1. Ver Razas")
        print("2. Agregar Raza")
        print("3. Modificar Raza")
        print("4. Consultar Raza")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            consultarRazasCargadas()
        elif opcion == '2':
            tipo_de_animal = input("Ingrese tipo de animal: ").lower()
            nombre_raza = input("Ingrese nombre de la raza: ").lower()
            agregarRaza(tipo=tipo_de_animal, raza=nombre_raza)
        elif opcion == '3':
            tipo_de_animal = input("Ingrese tipo de animal: ").lower()
            nombre_raza = input("Ingrese nombre de la raza: ").lower()
            consultarRaza(tipo=tipo_de_animal, nombre_raza=nombre_raza)
            modificarRaza( tipo_de_animal, nombre_raza)
        elif opcion == '4':
            tipo_de_animal = input("Ingrese tipo de animal: ").lower()
            nombre_raza = input("Ingrese nombre de la raza: ").lower()
            consultarRaza(tipo=tipo_de_animal, nombre_raza=nombre_raza)
        elif opcion == '0':
            menu_razas_abierto = False
        else:
            print("Opción no válida. Intente de nuevo.")

def menu_mascotas():
    menu_mascotas_abierto = True
    while menu_mascotas_abierto:
        print("\nMenú Mascotas:")
        print("1. Ver Mascotas")
        print("2. Agregar Mascotas")
        print("3. Modificar Mascotas")
        print("4. Consultar Mascotas")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            consultarMascotasCargadas()
        elif opcion == '2':
            tipo_de_animal = input("Ingrese tipo de animal: ").lower()
            nombre_raza = input("Ingrese nombre de la raza: ").lower()
            agregarMascota(tipo=tipo_de_animal, raza=nombre_raza)
        elif opcion == '3':
            id_mascota = input("Ingrese id mascota: ").lower()
            propietario = input("Ingrese nombre propietario: ").lower()
            modificarMascota(id_mascota, propietario)
        elif opcion == '4':
            id_mascota = input("Ingrese id mascota: ").lower()
            propietario = input("Ingrese nombre propietario: ").lower()
            consultarMascota(id_mascota, propietario)
        elif opcion == '0':
            menu_mascotas_abierto = False
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu_principal()