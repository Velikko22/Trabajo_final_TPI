
from Consulta import Consulta
from pathlib import Path

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

    def getHistorial(self):
        nombre_cliente = input("Ingrese el nombre del cliente: ").strip().lower()
        fecha_busqueda = input("Ingrese la fecha (DD-MM-YYYY): ").strip()
        nombre_mascota = input("Ingrese el nombre de la mascota: ").strip().lower()

        archivo_cliente = Path(f"../Datos archivos.txt/lista historial/{nombre_cliente}.txt")

        if not archivo_cliente.exists():
            print(f"No se encontro el archivo para el cliente: {nombre_cliente}")
            return False, None, None, None, None, None

        with open(archivo_cliente, "r", encoding="UTF-8") as file:
            lineas = file.readlines()
        indice = 0
        for linea in lineas:
            datos_consulta = eval(linea.strip())
            fecha_consulta = datos_consulta[0].split(' ')[0]
            nombre_mascota_consulta = datos_consulta[1].lower()

            if fecha_consulta == fecha_busqueda and nombre_mascota_consulta == nombre_mascota:
                print(f"Consulta encontrada: {datos_consulta}")
                return True, archivo_cliente,indice,nombre_cliente, fecha_busqueda, nombre_mascota
            indice += 1 #si se encuentra la consulta en linea 0 no llega aquí

        print("No se encontro ninguna Consulta que coincida")
        return False, None, None, None, None, None


    def modificarConsulta(self):
        consulta_encontrada, archivo_cliente, indice, nombre_cliente, fecha_busqueda, nombre_mascota = self.getHistorial()
        if consulta_encontrada:
            with open(archivo_cliente, "r", encoding="UTF-8") as file:
                lineas = file.readlines()

            datos_consulta = eval(lineas[indice].strip())
            print(f"Consulta encontrada: {datos_consulta}")
            respuesta = input("Modificar esta consulta? (S/N): ").strip().upper()
            if respuesta != 'S':
                return

            print("Modificar Consultas, en caso desee mantener el valor original anterior pulse tecla enter")
            nueva_fecha = input("Ingrese nueva fecha ").strip() or datos_consulta[0]
            nuevo_nombre_mascota = datos_consulta[1]
            nuevo_doctor = input("Ingrese nuevo doctor: ").strip() or datos_consulta[2]
            nuevo_id = datos_consulta[3]
            nuevo_diagnostico = input(f"Ingrese nuevo diagnostico (actual: {datos_consulta[4]}): ").strip() or datos_consulta[4]
            nuevo_historial = input(f"Ingrese nuevo historial medico (actual: {datos_consulta[5]}): ").strip() or datos_consulta[5]
            nueva_consulta = [nueva_fecha, nuevo_nombre_mascota, nuevo_doctor, nuevo_id, nuevo_diagnostico,
                              nuevo_historial]

            lineas[indice] = str(nueva_consulta) + '\n'

            with open(archivo_cliente, "w", encoding="UTF-8") as file:
                file.writelines(lineas)
            print("Consulta modificada y guardada ")

        else:
            print("No se encontró ninguna consulta que coincida.")

    def eliminarConsulta(self):
        consulta_encontrada, archivo_cliente, indice, nombre_cliente, fecha_busqueda, nombre_mascota = self.getHistorial()
        if consulta_encontrada:
            with open(archivo_cliente, "r", encoding="UTF-8") as file:
                lineas = file.readlines()

            datos_consulta = eval(lineas[indice].strip())
            print(f"Consulta encontrada: {datos_consulta}")

            respuesta = input("¿Desea eliminar esta consulta? (S/N): ").strip().upper()
            if respuesta != 'S':
                return

            del lineas[indice]

            with open(archivo_cliente, "w", encoding="UTF-8") as file:
                file.writelines(lineas)

            print("Consulta eliminada, archivo guardad")
        else:
            print("No se encontraron consultas que coincidan")


if __name__=="__main__":


    ficha = FichaMedica()
    #ficha.addHistorialConsulta()
    #ficha.getHistorial()
    ficha.modificarConsulta()