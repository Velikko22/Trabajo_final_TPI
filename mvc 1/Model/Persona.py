class Persona:
    def __init__(self, nombre="", telefono="", email="", direccion=""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def getNombre(self):
        return self.nombre

    def getTelefono(self):
        return self.telefono

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getDireccion(self):
        return self.direccion

    def setDireccion(self, direccion):
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, Tel: {self.telefono}, Email: {self.email}, Direccion: {self.direccion}"

    def __repr__(self):
        return self.__str__()