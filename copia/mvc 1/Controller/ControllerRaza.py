from Model.Raza import Raza
from View.ViewRaza import ViewRaza
from pathlib import Path
RUTA_RAZAS = Path('Datos archivos.txt//listas de razas')


class ControllerRaza:

    def __init__(self):
        self.lista_de_razas_disponibles = []
        self.lista_razas_objetos = []
        self.vista = ViewRaza()




    def cargarArchivoRaza(self):
        archivos = list(RUTA_RAZAS.glob('*'))
        for archivo in archivos:
            with (open(archivo,"r",encoding="UTF-8") as file):
                linea = file.readline()
                tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, state = linea.strip().split(";")
                self.lista_razas_objetos.append(Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza, esperanzaVidaRaza, state))

    def validarRaza(self, tipo, raza):
        for animal in self.lista_razas_objetos:
            if animal.tipoAnimal == tipo and animal.nombreRaza == raza:
                return True
        return False


    def validarIngresoState(self):
        while True:
            try:
                numero = int(input("Estado de la raza: 1-Activo/0-Inactivo "))
                if numero == 1 or numero == 0:
                    return numero
                else:
                    print("Ingrese un numero válido (1 o 0).")
            except ValueError:
                print("Ingrese un numero entero.")


    def buscarRaza(self):
        tipo = str(input("Ingrese el tipo de Animal: ")).lower()
        raza = str(input("Ingrese el nombre de la Raza: ")).lower()
        for animal in self.lista_razas_objetos:
            if animal.tipoAnimal == tipo and animal.nombreRaza == raza:
                if animal.state == 1:
                    self.vista.mensajeRazaEncontrada()
                    print(animal)
                elif animal.state == 0:
                    self.vista.MostrarRazaEliminada()


    def agregarRaza(self):
        tipo = str(input("Ingrese el tipo de Animal: ")).lower()
        raza = str(input("Ingrese el nombre de la Raza: ")).lower()
        continuar_carga = self.validarRaza(tipo,raza)
        if continuar_carga:
            print("Raza ya existente...probar con otra...")

        else:
            self.lista_razas_objetos = []
            tipoAnimal = tipo
            nombreRaza = raza
            tamanoRaza = input("Tamaño de la raza: ").lower()
            personalidadRaza = input("Personalidad de la raza: ").lower()
            pelajeRaza = input("Pelaje de la raza: ").lower()
            cuidadosRaza = input("Cuidados de la raza: ").lower()
            energiaRaza = input("Energía de la raza: ").lower()
            esperanzaVidaRaza = input("Esperanza de vida de la raza: ").lower()
            state = self.validarIngresoState()

            linea = f"{tipoAnimal};{nombreRaza};{tamanoRaza};{personalidadRaza};{pelajeRaza};{cuidadosRaza};{energiaRaza};" \
                    f"{esperanzaVidaRaza};{state}"
            nombre_archivo = f"{tipo}_{raza}.txt"
            lugar_y_nombre_archivo = RUTA_RAZAS / nombre_archivo

            with lugar_y_nombre_archivo.open("w", encoding="UTF-8") as file:
                file.write(linea)
            print("Archivo creado y guardado.")
        self.cargarArchivoRaza()


    def modificarRaza(self):
        tipo_de_animal = str(input("Ingrese el tipo de Animal: ")).lower()
        tipo_de_raza = str(input("Ingrese el nombre de la Raza: ")).lower()

        for cada_raza in self.lista_razas_objetos:
            if cada_raza.tipoAnimal == tipo_de_animal and cada_raza.nombreRaza == tipo_de_raza :
                print(cada_raza.tamanoRaza)
                print(type(cada_raza))
                nuevo_tamanoRaza = input("Nuevo Tamaño: ")
                nuevo_personalidadRaza = input("Nueva Personalidad: ")
                nuevo_pelajeRaza = input("Nuevo Pelaje: ")
                nuevo_cuidadosRaza = input("Nuevo Cuidado: ")
                nuevo_energiaRaza = input("Nueva Energía: ")
                nuevo_esperanzaVidaRaza = input("Nueva Esperanza de Vida: ")
                nuevo_state = self.validarIngresoState()


                cada_raza.tamanoRaza = tipo_de_animal
                cada_raza.nombreRaza = tipo_de_raza
                cada_raza.tamanoRaza = nuevo_tamanoRaza
                cada_raza.personalidadRaza = nuevo_personalidadRaza
                cada_raza.pelajeRaza = nuevo_pelajeRaza
                cada_raza.cuidadosRaza = nuevo_cuidadosRaza
                cada_raza.energiaRaza = nuevo_energiaRaza
                cada_raza.esperanzaVidaRaza = nuevo_esperanzaVidaRaza
                cada_raza.state = nuevo_state

                linea = f"{cada_raza.tipoAnimal};{cada_raza.nombreRaza};{cada_raza.tamanoRaza};{cada_raza.personalidadRaza};{cada_raza.pelajeRaza};{cada_raza.cuidadosRaza};{cada_raza.energiaRaza};" \
                        f"{cada_raza.esperanzaVidaRaza};{cada_raza.state}"
                nombre_archivo = f"{tipo_de_animal}_{tipo_de_raza}.txt"
                lugar_y_nombre_archivo = RUTA_RAZAS / nombre_archivo

                with lugar_y_nombre_archivo.open("w", encoding="UTF-8") as file:
                    file.write(linea)
                print("Archivo creado y guardado.")

        else:
            self.vista.mensajeRazaNoencontrada()



    def eliminarRaza(self):
        eliminar_tipo = str(input("Ingrese el tipo de Animal: ")).lower()
        eliminar_raza = str(input("Ingrese el nombre de la Raza: ")).lower()
        for cada_raza in self.lista_razas_objetos:
            if cada_raza.tipoAnimal ==  eliminar_tipo and cada_raza.nombreRaza ==  eliminar_raza:
                cada_raza.state = self.validarIngresoState()

                linea = f"{cada_raza.tipoAnimal};{cada_raza.nombreRaza};{cada_raza.tamanoRaza};{cada_raza.personalidadRaza};{cada_raza.pelajeRaza};{cada_raza.cuidadosRaza};{cada_raza.energiaRaza};" \
                        f"{cada_raza.esperanzaVidaRaza};{cada_raza.state}"
                nombre_archivo = f"{ eliminar_tipo}_{ eliminar_raza}.txt"
                lugar_y_nombre_archivo = RUTA_RAZAS / nombre_archivo

                with lugar_y_nombre_archivo.open("w", encoding="UTF-8") as file:
                    file.write(linea)
                print("Archivo Modificado y Cambiado de estado.")

    def listarRazasDisponibles(self):
        self.vista.mostrarPantallaRazasDisponibles(self.lista_razas_objetos)



