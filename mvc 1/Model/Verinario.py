from Model.Persona import Persona


class Veterinario(Persona):
    def __init__(self, nombre, telefono, cargo):
        super().__init__(nombre, telefono)
        self.cargo = cargo

    def getNombreVeterinario(self):
        return self.nombre

    def getTelefonoVeterinario(self):
        return self.telefono

    def getCargoVeterinario(self):
        return self.cargo

    def setCargoVeterinario(self, cargo):
        self.cargo = cargo

    def __str__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Tel: {self.telefono}"

    def __repr__(self):
        return self.__str__()