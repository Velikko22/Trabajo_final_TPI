from Model.Mascota import Mascota
from View.ViewMascota import ViewMascota
from Controller.ControllerRaza import ControllerRaza
from pathlib import Path

RUTA_MASCOTAS = Path('Datos archivos.txt//listas de mascotas')


class ControllerMascota:
    def __init__(self):
        self.lista_mascotas_objeto = []
        self.vista = ViewMascota()
        self.controladorRaza = ControllerRaza()



    def cargarArchivoMascota(self):
        with open(RUTA_MASCOTAS,"r", encoding="UTF-8") as file:
            archivo = file.readlines()
            for linea in archivo:
                tipoAnimalRaza, nombreRazaAnimal, identificador, propietario, nombreAnimal, detalleMascota, stateMascota =linea.strip().split(";")
                self.lista_mascotas_objeto.append(Mascota(tipoAnimalRaza, nombreRazaAnimal,identificador,propietario, nombreAnimal,  detalleMascota, stateMascota))




    def agregarMascota(self):
        tipo_de_animal = str(input("Ingrese el tipo de Animal: ")).lower()
        tipo_de_raza = str(input("Ingrese el nombre de la Raza: ")).lower()
        continuar_carga = self.controladorRaza.validarRaza(tipo_de_animal,tipo_de_raza)
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


