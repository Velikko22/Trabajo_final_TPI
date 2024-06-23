from Controller.ControllerPersona import ControllerPersona
from Controller.ControllerRaza import ControllerRaza
from Controller.ControllerMascota import ControllerMascota

class ControllerMenuClienteVeterinario:
    def __init__(self):
        self.controladorRaza = ControllerRaza()
        self.controladorMascota = ControllerMascota(self.controladorRaza)
        self.controladorPersona = ControllerPersona(self.controladorMascota, self.controladorRaza)

    def menuPersonas(self):
        opcion = int(input("Opciones "))
        self.controladorRaza.cargarArchivoRaza()

        if opcion == 1:
            self.controladorPersona.cargarArchivosPersonas()
            self.controladorPersona.modificarCliente()

        elif opcion == 2:
            self.controladorPersona.cargarArchivosPersonas()
            self.controladorPersona.mostrarClientes()
            self.controladorPersona.mostrarVeterinarios()
            self.controladorPersona.registrarCliente()
            self.controladorPersona.registrarVeterinario()