
from Consulta import Consulta

class FichaMedica:
    def __init__(self, identificador=1):
        self.estado = True
        self.identificador = identificador

    def crearFichaMedica(self):
        #el nombre del archivo debe ser el nombre de cliente
        pass

    def addHistorialConsulta(self):

        #Comprobar si esta la ficha medica creada con el nombre del cliente
        consulta = Consulta(cliente = "123_firu",mascota = "Firulais", veterinario = "Dr. López",diagnostico = "Diagnóstico de ejemplo",
                            historialMedico = "Historial médico de ejemplo")
        historial = consulta.crearNuevoHistorial()
        nombre_archivo = f"{historial[3]}"

        ruta = "../Datos archivos.txt/lista historial"
        try:
            with open(f"{ruta}//{nombre_archivo}.txt","a+", encoding="UTF-8") as file:
                file.write(str(historial) + "\n")
                print("Consulta Agregada con Éxito")
        except:
            print("No existe el archivo ")
            with open(f"{ruta}//{nombre_archivo}.txt","a+", encoding="UTF-8") as file:
                file.write(str(historial))
                print("Consulta Creada y agregada con Éxito")


    def buscarIdentificador(self):
        pass
    def guardarArchivo(self):
        pass

    def getFecha(self):
        self.fechaformateada_dias = self.fecha.strftime("%d/%m/%Y")
        self.fechaformateada_horas = self.fecha.strftime("%H:%M")
        return f"el dia es: {self.fechaformateada_dias}, y la hora es: {self.fechaformateada_horas}"
    
    def __str__(self):
        return "Esta es la clase ficha"

if __name__=="__main__":


    ficha = FichaMedica()
    ficha.addHistorialConsulta()