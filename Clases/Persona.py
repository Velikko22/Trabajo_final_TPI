class Personas:
    def __init__(self, nombre="", telefono="", email="", direccion=""):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    def __str__(self):
        return f"Nombre: {self.nombre}, Tel: {self.telefono}, Email: {self.email}, Direccion: {self.direccion}"
    
    def __repr__(self):
        return self.__str__()

