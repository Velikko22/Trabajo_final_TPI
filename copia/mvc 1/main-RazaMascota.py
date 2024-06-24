from Controller.ControllerRaza import ControllerRaza
from Controller.ControllerMascota import ControllerMascota
from Controller.ControllerMenuRazaMascota import ControllerMenuRazaMascota
from pathlib import Path
RUTA_RAZAS = Path('Datos archivos.txt//listas de razas')

def menu():

    #Sentencias obligatorias de inicio
    controladorMenu = ControllerMenuRazaMascota()
    controladorMenu.iniciarCarga()

    controladorMenu.mostrarMenu()




if __name__ == "__main__":
    menu()
