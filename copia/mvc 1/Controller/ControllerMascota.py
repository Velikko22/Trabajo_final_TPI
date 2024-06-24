from Model.Mascota import Mascota
from Controller.ControllerRaza import ControllerRaza
from View.ViewMascota import ViewMascota
from pathlib import Path

from interfaz.Interfaz import interfaz

vista = interfaz()

RUTA_MASCOTAS = Path('Datos archivos.txt/lista mascotas')


class ControllerMascota:
    def __init__(self,controladorRaza):
        self.lista_mascotas_objeto = []
        self.vista = ViewMascota()
        self.controladorRaza = controladorRaza





    def cargarArchivoMascota(self):
        archivos = list(RUTA_MASCOTAS.glob('*'))
        for archivo in archivos:
            with (open(archivo,"r", encoding="UTF-8") as file):
                linea = file.readline()
                tipoAnimalRaza,nombreRazaAnimal,identificador,propietario,nombreAnimal, detalleMascota,stateMascota = linea.strip().split(";")
                self.lista_mascotas_objeto.append(Mascota(tipoAnimalRaza,nombreRazaAnimal,identificador,propietario,nombreAnimal, detalleMascota,stateMascota))

    def agregarMascota(self):
        tipo_de_animal = interzaf
        tipo_de_raza = str(input("Ingrese el nombre de la Raza: ")).lower()
        continuar_carga = self.controladorRaza.validarRaza(tipo=tipo_de_animal, raza=tipo_de_raza)
        if continuar_carga:
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
        buscar_nombre_mascota =input("Ingrese nombre mascota ")
        buscar_nombre_propietario = input("Ingrese nombre propietario ")
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

        if archivo_path.exists():
            with open(archivo_path, "r", encoding="UTF-8") as file:
                archivo = file.readline()
                datos = archivo.split(";")
                tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, historial, stateMascota = datos
            mascota_objeto = Mascota(tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal,
                                     historial, stateMascota)
            self.lista_mascotas_objeto.append(mascota_objeto)
            continuar_modificacion = True
            while continuar_modificacion:
                try:
                    print("===============")
                    print("Que desea modificar? ")
                    print(
                        "1 Tipo Animal\n 2 Nombre Raza \n 3 Identificador Mascota\n 4 Nombre Propietario\n 5 Nombre Mascota\n 6 historial\n 7 stateMascota\n 0 Salir y Guardar cambios")
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
                        nuevo_nombreAnimal = input("Nuevo nombre de animal: ").lower()
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
                        if self.controladorRaza.validarRaza(mascota_objeto.get_tipoAnimalRaza(),
                                                            mascota_objeto.get_nombreRazaAnimal()):

                            archivo_path.unlink()


                            nuevo_nombre_archivo = f"{mascota_objeto.get_identificador()}_{mascota_objeto.get_propietario()}.txt"
                            nuevo_archivo_path = RUTA_MASCOTAS / nuevo_nombre_archivo


                            with open(nuevo_archivo_path, "w", encoding="UTF-8") as file:
                                file.write(
                                    f"{mascota_objeto.get_tipoAnimalRaza()};{mascota_objeto.get_nombreRazaAnimal()};"
                                    f"{mascota_objeto.get_identificador()};{mascota_objeto.get_propietario()};"
                                    f"{mascota_objeto.get_nombreAnimal()};{mascota_objeto.get_historial()};"
                                    f"{mascota_objeto.get_stateMascota()}")
                            print("Cambios guardados exitosamente.")


                            #Recargo la Lista para seguir operando
                            self.lista_mascotas_objeto = []
                            self.cargarArchivoMascota()


                            continuar_modificacion = False
                        else:
                            print("La raza modificada no existe. No se guardaron los cambios. Debe Crearla! ")

                except ValueError:
                    print("Por favor, ingrese un número válido.")