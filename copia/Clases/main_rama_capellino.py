from Persona import Personas
from Veterinarios import Veterinario
from Cliente import Cliente

lista_personas = []
nombresMascota = []
tipoMascota = []

def menu():
    print("Bienvenido, ¿Que desea hacer?")
    print("[1] - Registrar cliente")
    print("[2] - Ver lista de clientes")
    print("[3] - Agregar veterinario")
    print("[4] - Ver lista de veterinarios")
    print("[9] - Salir")
    
    opcion = int(input("Ingrese opcion: "))
    return opcion

def ingresos_de_datos(opcion):
    
    nombre = input("Ingrese nombre completo: ")
    telefono = input("Ingrese telefono contacto: ")
    
    if opcion == 1:
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
        
        return nombre, telefono, email, direccion, cantidad, nombresMascota, tipoMascota
    
    if opcion == 3:
        cargo = input("Ingrese Cargo del Veterinario: ")
        return nombre, telefono, cargo

def carga_de_persona(opcion):
    if opcion == 1 or opcion == 3:
        while True:
            if opcion == 1:
                nombre, telefono, email, direccion, cantidad, nombresMascota, tipoMascota = ingresos_de_datos(opcion)
                cliente = Cliente(nombre, telefono, email, direccion, cantidad, nombresMascota, tipoMascota)
                with open("TrabajoFinal/Trabajo_final_TPI/Datos archivos.txt/clientes.txt", "a") as archivo:
                    archivo.write(f"{cliente}\n")
            
            if opcion == 3:
                nombre, telefono, cargo = ingresos_de_datos(opcion)
                veterinario = Veterinario(nombre, telefono, cargo)
                with open("TrabajoFinal/Trabajo_final_TPI/Datos archivos.txt/veterinarios.txt", "a") as archivo:
                    archivo.write(f"{veterinario}\n")
            
            while True:
                salida = str(input("¿Desea agregar otra persona? [S][N]: "))
                if salida.lower() == "n" or salida.lower() == "s":
                    break
                else:
                    print("comando no valido.")
            if salida.lower() == "n":
                break

    if opcion == 2:
        with open("TrabajoFinal/Trabajo_final_TPI/Datos archivos.txt/clientes.txt", "r") as archivo:
            for linea in archivo:
                print(linea.strip())
                
    if opcion == 4:
        with open("TrabajoFinal/Trabajo_final_TPI/Datos archivos.txt/veterinarios.txt", "r") as archivo:
            for linea in archivo:
                print(linea.strip())

def main():
    while True:
        opcion = menu()
        if opcion == 9:
            break
        else:
            carga_de_persona(opcion)

if __name__ == "__main__":
    main()
