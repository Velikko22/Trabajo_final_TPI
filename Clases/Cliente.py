from .Persona import Personas

class Cliente(Personas):
    def __init__(self, nombre, telefono, email, direccion, cantidad, nombreMascota, tipoMascotas):
        super().__init__(nombre, telefono, email, direccion)
        self.cantidad = cantidad
        self.nombreMascota = nombreMascota
        self.tipoMascotas = tipoMascotas

    def __str__(self):
        return f"Nombre: {self.nombre}, Tel: {self.telefono}, Email: {self.email}, Direccion: {self.direccion}, Cantidad de Mascotas: {self.cantidad}, Mascotas: {self.nombreMascota}, {self.tipoMascotas}"
    
    def __repr__(self):
        return self.__str__()
