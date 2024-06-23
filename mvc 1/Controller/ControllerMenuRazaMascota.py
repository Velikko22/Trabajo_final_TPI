from View.ViewMenuRazaMascota import ViewMenuRazaMascota
from Controller.ControllerRaza import ControllerRaza
from Controller.ControllerMascota import ControllerMascota

class ControllerMenuRazaMascota:
    def __init__(self):
        self.vista = ViewMenuRazaMascota()
        self.controladorRaza = ControllerRaza()
        self.controladorMascota = ControllerMascota(self.controladorRaza)

    def iniciarCarga(self):
        self.controladorRaza.cargarArchivoRaza()
        self.controladorMascota.cargarArchivoMascota()

    def mostrarMenu(self):
        while True:
            self.vista.mostrarOpcionesMenuRaza()
            opcion_menu = int(input("Ingrese opcion "))
            if opcion_menu == 1:
                print(self.controladorRaza.lista_razas_objetos)
                self.controladorRaza.listarRazasDisponibles()
            elif opcion_menu == 2:
                self.controladorRaza.buscarRaza()
            elif opcion_menu == 3:
                self.controladorRaza.modificarRaza()
            elif opcion_menu == 4:
                self.controladorRaza.agregarRaza()
            elif opcion_menu == 5:
                self.controladorRaza.eliminarRaza()
            elif opcion_menu == 6:
                self.controladorMascota.buscarMascota()
            elif opcion_menu == 7:
                self.controladorMascota.agregarMascota()
            elif opcion_menu == 8:
                self.controladorMascota.modificarMascota()
