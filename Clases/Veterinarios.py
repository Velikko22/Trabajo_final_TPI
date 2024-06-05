from Persona import Personas

class Veterinario(Personas):
    def __init__(self, nombre, telefono, cargo):
        super().__init__(nombre, telefono)
        self.cargo = cargo

    def __str__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Tel: {self.telefono}"
    
    def __repr__(self):
        return self.__str__()
