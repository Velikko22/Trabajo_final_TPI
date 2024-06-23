from Model.Persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, telefono, email, direccion, cantidad, nombreMascota, tipoMascotas):
        super().__init__(nombre, telefono, email, direccion)
        self.cantidad = cantidad
        self.nombreMascota = nombreMascota
        self.tipoMascotas = tipoMascotas

    def getNombreCliente(self):
        return self.nombre

    def getTelefonoCliente(self):
        return self.telefono

    def getEmailCliente(self):
        return self.email

    def getDireccionCliente(self):
        return self.direccion

    def getCantidadMascotas(self):
        return self.cantidad

    def setCantidadMascotas(self, cantidad):
        self.cantidad = cantidad

    def getNombreMascotas(self):
        return self.nombreMascota

    def setNombreMascotas(self, nombreMascota):
        self.nombreMascota = nombreMascota

    def getTipoMascota(self):
        return self.tipoMascotas

    def setTipoMascota(self, tipoMascota):
        self.tipoMascotas = tipoMascota

    def __str__(self):
        return f"Nombre: {self.nombre}, Tel: {self.telefono}, Email: {self.email}, Direccion: {self.direccion}, Cantidad de Mascotas: {self.cantidad}, Mascotas: {self.nombreMascota}, {self.tipoMascotas}"

    def __repr__(self):
        return self.__str__()