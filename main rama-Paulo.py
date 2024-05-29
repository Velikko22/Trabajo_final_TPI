from Clases.Raza import Raza

def main():
    raza = Raza("","","","","","","","","") #Inicio una clase vacía para poder acceder a los metodos
    opcion_tipo_animal  =str(input("Tipo de Animal ")).lower()
    opcion_raza_buscar = str(input("Raza a buscar ")).lower()
    raza.buscarRaza(opcion_tipo_animal,opcion_raza_buscar)

    op = input("Desea crear nueva raza? S/N").capitalize()
    if op == "S":
        raza.altaRaza()
    else:
        print("saliendo... ")


if __name__ == "__main__":
    main()

