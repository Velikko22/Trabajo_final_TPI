class Mascota():
    def __init__(self, tipoAnimalRaza, nombreRazaAnimal,identificador,propietario, nombreAnimal,  detalleMascota, stateMascota):
        self.tipoAnimalRaza = tipoAnimalRaza
        self.nombreRazaAnimal = nombreRazaAnimal
        self.identificador = identificador
        self.propietario = propietario
        self.nombreAnimal = nombreAnimal
        self.detalleMascota = detalleMascota
        self.stateMascota = int(stateMascota)

    def mascotaActiva(self):
        if self.stateMascota == 1:
            return True

    def get_tipoAnimalRaza(self):
        return self.tipoAnimalRaza

    def get_nombreRazaAnimal(self):
        return self.nombreRazaAnimal

    def get_identificador(self):
        return self.identificador


    def get_propietario(self):
        return self.propietario

    def get_nombreAnimal(self):
        return self.nombreAnimal

    def get_historial(self):
        return self.detalleMascota

    def get_stateMascota(self):
        return self.stateMascota

    def set_tipoAnimalRaza(self, tipoAnimalRaza):
        self.tipoAnimalRaza = tipoAnimalRaza

    def set_nombreRazaAnimal(self, nombreRazaAnimal):
        self.nombreRazaAnimal = nombreRazaAnimal

    def set_identificador(self, identificador):
        self.identificador = identificador

    def set_propietario(self, propietario):
        self.propietario = propietario

    def set_nombreAnimal(self, nombreAnimal):
        self.nombreAnimal = nombreAnimal

    def set_historial(self, detalleMascota):
        self.detalleMascota = detalleMascota

    def set_stateMascota(self, stateMascota):
        self.stateMascota = stateMascota

    def __repr__(self):
        return (f"{self.tipoAnimalRaza}, {self.nombreRazaAnimal}, {self.identificador}, {self.propietario}, "
                f"{self.nombreAnimal}, {self.detalleMascota},{self.stateMascota}")
