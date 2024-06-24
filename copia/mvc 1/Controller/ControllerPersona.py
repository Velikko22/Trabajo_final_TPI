from Model.Persona import Persona
from Model.Cliente import Cliente
from Model.Verinario import Veterinario
from View.ViewPersona import ViewPersona
from Controller.ControllerMascota import ControllerMascota
from Controller.ControllerRaza import ControllerRaza

class ControllerPersona:
    def __init__(self, controladorMascota, controladorRaza):
        self.lista_personas = []
        self.nombresMascota = []
        self.tipoMascota = []
        self.lista_veterinarios_objeto = []
        self.vistaPersonal = ViewPersona()
        self.controladorMascota = controladorMascota
        self.controladorRaza = controladorRaza


    def menu(self):
        print("Bienvenido, ¿Que desea hacer?")
        print("[1] - Registrar cliente")
        print("[2] - Ver lista de clientes")
        print("[3] - Agregar veterinario")
        print("[4] - Ver lista de veterinarios")
        print("[9] - Salir")

        opcion = int(input("Ingrese opcion: "))
        return opcion




    def cargarArchivosPersonas(self):
        #cargar Veterinarios
        with open("Datos archivos.txt/veterinarios.txt", "r") as file:
            archivo = file.readlines()
            for linea in archivo:
                nombre, telefono, cargo = linea.strip().split(";")
                self.lista_veterinarios_objeto.append(Veterinario(nombre,telefono,cargo))

        #Cargar Archivo Clientes
        with open("Datos archivos.txt/clientes.txt", "r") as file:
            archivo = file.readlines()
            for linea in archivo:
                nombre,telefono,email,direccion,cantidad,nombreMascota,tipoMascotas = linea.strip().split(";")
                self.lista_personas.append(Cliente(nombre,telefono,email,direccion,cantidad,nombreMascota,tipoMascotas))


    def mostrarClientes(self):
        for persona in self.lista_personas:
            print(persona)


    def mostrarVeterinarios(self):
        for verinario in self.lista_veterinarios_objeto:
            print(verinario)


    def ingreso_de_datos(self):
        nombre = input("Ingrese nombre completo: ")
        telefono = input("Ingrese telefono contacto: ")
        return nombre,telefono

    def registrarVeterinario(self):
        nombre,telefono = self.ingreso_de_datos()
        cargo = input("Ingrese Cargo del Veterinario: ")
        veterinario = f"{nombre};{telefono};{cargo}"
        with open("Datos archivos.txt/veterinarios.txt", "a") as archivo:
            archivo.write(f"{veterinario}\n")
        self.lista_veterinarios_objeto=[]
        self.lista_personas=[]
        self.cargarArchivosPersonas()




    def registrarCliente(self):
        nombre, telefono = self.ingreso_de_datos()
        email = input("Ingrese email contacto: ")
        direccion = input("Ingrese direccion: ")
        cantidad = int(input("Ingrese la cantidad de mascotas: "))
        nombresMascota = []
        tipoMascota = []
        for i in range(cantidad):
            mascotanombre = str(input("Ingrese el nombre de la mascota: "))
            mascotatipo = str(input("Ingrese el tipo de mascota: "))
            nombresMascota.append(mascotanombre)
            tipoMascota.append(mascotatipo)
            self.controladorMascota.agregarMascotaCliente(tipo_animal=mascotatipo, nombreAnimal=mascotanombre,
                                                          propietario=nombre)
        cliente = f"{nombre};{telefono};{email};{direccion};{cantidad};{nombresMascota};{tipoMascota}"
        with open("Datos archivos.txt/clientes.txt", "a") as archivo:
            archivo.write(f"{cliente}\n")

        self.lista_veterinarios_objeto = []
        self.lista_personas = []
        self.cargarArchivosPersonas()





    def modificarCliente(self):
        pass







