from Persona import Personas

lista_personas = []

def menu():
    print("Bienvenido, ¿Que desea hacer?")
    print("[1] - Registrar cliente")
    print("[2] - Ver lista de clientes")
    print("[3] - Agregar veterinario")
    print("[4] - Ver lista de veterinarios")
    print("[9] - Salir")
    
    opcion = int(input("Ingrese opcion: "))
    return opcion

def carga_de_persona(opcion):
    
    if opcion == 1 or opcion == 3:
        
        while True:
            
            nombre = input("Ingrese nombre completo: ")
            telefono = input("Ingrese telefono contacto: ")
            email = input("Ingrese email contacto: ")
            direccion = input("Ingrese direccion: ")
            
            if opcion == 1:
                mascota = None
                with open("TrabajoFinal/Trabajo_final_TPI/Datos archivos.txt/clientes.txt", "a") as archivo:
                    archivo.write(f"{nombre},{telefono},{email},{direccion}\n")
                    
            if opcion == 3:
                cargo = input("Ingrese Cargo del Veterinario: ")
                with open("TrabajoFinal/Trabajo_final_TPI/Datos archivos.txt/veterinarios.txt", "a") as archivo:
                    archivo.write(f"{nombre},{telefono},{email},{direccion},{cargo}\n")
            
            while True:
                salida=str(input("¿Desea agregar otra persona? [S][N]: "))
                if salida.lower() == "n" or salida.lower() == "s":
                    break
                else:
                    print("comando no valido.")
            if salida.lower() == "n":
                break

    if opcion == 2:  

        with open("TrabajoFinal/Trabajo_final_TPI/Datos archivos.txt/clientes.txt", "r") as archivo:
            for linea in archivo:
                nombre,telefono,email,direccion = linea.strip().split(",")
                lista_personas.append(Personas(nombre,telefono,email,direccion))
            print(lista_personas)
        


def main():
    while True:
        opcion = menu()
        if opcion == 9:
            break
        else:
            carga_de_persona(opcion)
        

if __name__ == "__main__":
    main()
