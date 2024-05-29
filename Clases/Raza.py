import os

RUTA = r'C:\Users\Usuario\PycharmProjects\TPIP2L2_2024\Trabajo_final_TPI\Datos archivos.txt\listas de razas'


class Raza:
    def __init__(self, tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,
                 esperanzaVidaRaza, state):
        self.tipoAnimal = tipoAnimal
        self.nombreRaza = nombreRaza
        self.tamanoRaza = tamanoRaza
        self.personalidadRaza = personalidadRaza
        self.pelajeRaza = pelajeRaza
        self.cuidadosRaza = cuidadosRaza
        self.energiaRaza = energiaRaza
        self.esperanzaVidaRaza = esperanzaVidaRaza
        self.state = state



    def buscarRaza(self,tipo,raza):
        """
        Recibe tipo y raza. Busca la raza en los archivos txt de la carpeta lista de razas,
        Si no se encuentra la raza genera un print de no encontrado
        """
        archivo_a_buscar = f"{tipo}_{raza}.txt"

        archivos = os.listdir(RUTA)
        for archivo in archivos:
            if archivo == archivo_a_buscar:
                ruta_completa = os.path.join(RUTA, archivo)
                print(f"Archivo encontrado: {ruta_completa}")
                with open(ruta_completa, 'r', encoding="UTF-8") as file:
                    data = file.read().strip().split(';')
                    print(data)
                    return data
        print(f"{tipo.capitalize()} y {raza.capitalize()} no encontrados")


    def altaRaza(self):
        """
        Crea un txt con los campos de la raza ingresado por el usuario,
        crea el archivo en la RUTA global y devuelve una lista
        """
        tipoAnimal= input("Ingrese Tipo: ").lower()
        nombreRaza= input("Ingrese Nombre Raza: ").lower()
        tamanoRaza = input("Ingrese tamaño: ").lower()
        personalidadRaza = input("Ingrese personalidad: ").lower()
        pelajeRaza = input("Ingrese pelaje: ").lower()
        cuidadosRaza = input("Ingrese cuidados: ").lower()
        energiaRaza = input("Ingrese energía: ").lower()
        esperanzaVidaRaza = input("Ingrese esperanza de vida: ").lower()
        state = input("Ingrese estado: ").lower()

        nueva_raza = Raza(tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,
                          esperanzaVidaRaza, state)

        archivo_a_guardar = f"{tipoAnimal}_{nombreRaza}.txt"
        ruta_completa = os.path.join(RUTA, archivo_a_guardar)
        with open(ruta_completa, 'w',encoding="UTF-8") as file:
            file.write(';'.join(
                [tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,
                 esperanzaVidaRaza, state]))
        print("ARCHIVO Creado, Raza agregada ")
        return nueva_raza

    def modificarRaza(self,tipo, raza):
        archivo_a_buscar = f"{tipo}_{raza}.txt"

        archivos = os.listdir(RUTA)
        for archivo in archivos:
            if archivo == archivo_a_buscar:
                ruta_completa = os.path.join(RUTA, archivo)
                print(f"Archivo encontrado: {ruta_completa}")
                with open(ruta_completa, 'r', encoding="UTF-8") as file:
                    data = file.read().strip().split(';')
                    print(data)
                    return data
        print(f"{tipo.capitalize()} y {raza.capitalize()} no encontrados")




    def get_tipoAnimal(self):
        return self.tipoAnimal

    def set_tipoAnimal(self, tipoAnimal):
        self.tipoAnimal = tipoAnimal

    def get_nombreRaza(self):
        return self.nombreRaza

    def set_nombreRaza(self, nombreRaza):
        self.nombreRaza = nombreRaza

    def get_tamanoRaza(self):
        return self.tamanoRaza

    def set_tamanoRaza(self, tamanoRaza):
        self.tamanoRaza = tamanoRaza

    def get_personalidadRaza(self):
        return self.personalidadRaza

    def set_personalidadRaza(self, personalidadRaza):
        self.personalidadRaza = personalidadRaza

    def get_pelajeRaza(self):
        return self.pelajeRaza

    def set_pelajeRaza(self, pelajeRaza):
        self.pelajeRaza = pelajeRaza

    def get_cuidadosRaza(self):
        return self.cuidadosRaza

    def set_cuidadosRaza(self, cuidadosRaza):
        self.cuidadosRaza = cuidadosRaza

    def get_energiaRaza(self):
        return self.energiaRaza

    def set_energiaRaza(self, energiaRaza):
        self.energiaRaza = energiaRaza

    def get_esperanzaVidaRaza(self):
        return self.esperanzaVidaRaza

    def set_esperanzaVidaRaza(self, esperanzaVidaRaza):
        self.esperanzaVidaRaza = esperanzaVidaRaza

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state= state


    def __repr__(self):
        return f" {self.tipoAnimal}, {self.nombreRaza}, {self.tamanoRaza}, {self.personalidadRaza}, {self.pelajeRaza}, {self.cuidadosRaza}, " \
               f"{self.energiaRaza}, {self.esperanzaVidaRaza}, {self.state}"



