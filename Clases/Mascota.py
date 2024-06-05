<<<<<<< HEAD
class Mascota:
    def __init__(self, nombre, especie, raza, propietario, historial, identificador, state):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.propietario = propietario
        self.historial = historial
        self.identificador = identificador
        self.state = state

    def buscarMascota(self):
        pass
    def altaMascota(self):
        pass
    def modificarMascota(self):
        pass




    def __repr__(self):
        return f"{self.nombre}, {self.especie}, {self.raza}, {self.propietario}, {self.historial},{self.identificador}, {self.state}"
=======
class Mascota():
    def __init__(self, tipoAnimalRaza, nombreRazaAnimal,identificador,propietario, nombreAnimal,  historial, stateMascota):
        self.tipoAnimalRaza = tipoAnimalRaza
        self.nombreRazaAnimal = nombreRazaAnimal
        self.identificador = identificador
        self.propietario = propietario
        self.nombreAnimal = nombreAnimal
        self.historial = historial
        self.stateMascota = stateMascota



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
        return self.historial

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

    def set_historial(self, historial):
        self.historial = historial

    def set_stateMascota(self, stateMascota):
        self.stateMascota = stateMascota

    def __repr__(self):
        return (f"{self.tipoAnimalRaza}, {self.nombreRazaAnimal}, {self.identificador}, {self.propietario}, "
                f"{self.nombreAnimal}, {self.historial},{self.stateMascota}")
>>>>>>> a0ab84d9beeecf2df235349af1796fb6bcb87619
