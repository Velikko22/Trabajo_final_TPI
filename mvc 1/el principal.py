from Controller.ControllerRaza import ControllerRaza
from pathlib import Path
RUTA_RAZAS = Path('Datos archivos.txt//listas de razas')

def menu():

    #Sentencias obligatorias de inicio
    controlador = ControllerRaza()
    controlador.cargarArchivoRaza()
    controlador.mostrarMenu()




if __name__ == "__main__":
    menu()
