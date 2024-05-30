from Clases.Raza2 import Raza
from Clases.Mascota2 import Mascota
import os

lista_objetos_raza = []
RUTA = r'Datos archivos.txt\listas de razas'



def buscadorRaza(tipo,raza):
    """Buscador de razas solo devuelve true o false, su uso es para controlar errores"""
    archivo_a_buscar = f"{tipo}_{raza}.txt"
    archivos = os.listdir(RUTA)
    for archivo in archivos:
        if archivo == archivo_a_buscar:
            print("Encontrado")
            return True


    print("NO ENCONTRADO")
    return False

def buscarRaza(tipo, raza):
    """
    Recibe tipo y raza. Busca la raza en los archivos txt de la carpeta lista de razas
    """
    archivo_a_buscar = f"{tipo}_{raza}.txt"

    archivos = os.listdir(RUTA)
    for archivo in archivos:
        if archivo == archivo_a_buscar:
            ruta_completa = os.path.join(RUTA, archivo)
            print(f"Archivo encontrado en: {ruta_completa}")
            with open(ruta_completa, 'r', encoding="UTF-8") as file:
                data = file.read().strip().split(';')
                print(data)
                return data
    print(f"{tipo.capitalize()} y {raza.capitalize()} no encontrados")
    return False

def agregarRaza(nueva_busqueda_tipo,nueva_busqueda_raza):
    """"Crear Raza nueva"""
    lista_objetos_raza.clear()
    tipo_nueva_raza =nueva_busqueda_tipo
    nombre_nueva_raza =nueva_busqueda_raza
    tamanoRaza = input("Ingrese tamaño: ").lower()
    personalidadRaza = input("Ingrese personalidad: ").lower()
    pelajeRaza = input("Ingrese pelaje: ").lower()
    cuidadosRaza = input("Ingrese cuidados: ").lower()
    energiaRaza = input("Ingrese energía: ").lower()
    esperanzaVidaRaza = input("Ingrese esperanza de vida: ").lower()
    state = input("Ingrese estado: ").lower()

    lista_objetos_raza.append(Raza(tipo_nueva_raza , nombre_nueva_raza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,
                      esperanzaVidaRaza, state))
    nombre_guardado_archivo = f"{tipo_nueva_raza}_{nombre_nueva_raza}.txt"
    ruta_completa_archivo = os.path.join(RUTA,nombre_guardado_archivo)
    print(ruta_completa_archivo)
    file =open(f"{ruta_completa_archivo}","w", encoding="UTF-8")
    linea = f"{tipo_nueva_raza};{nombre_nueva_raza};{tamanoRaza};{personalidadRaza};{pelajeRaza};{cuidadosRaza};{energiaRaza};{esperanzaVidaRaza};{state}"
    file.writelines(linea)
    print(f"{tipo_nueva_raza}_{nombre_nueva_raza}.txt Archivo Cargado con Exito")
    file.close()

def modificarRaza(tipo,raza):
    aux = buscadorRaza(tipo,raza)
    if aux:
        print("Buscando raza...")
        archivo_a_buscar = f"{tipo}_{raza}.txt"
        archivos = os.listdir(RUTA)
        for archivo in archivos:
            if archivo == archivo_a_buscar:
                ruta_completa = os.path.join(RUTA, archivo)
                tipo_nueva_raza = tipo
                nombre_nueva_raza = raza
                tamanoRaza = input("Ingrese tamaño: ").lower()
                personalidadRaza = input("Ingrese personalidad: ").lower()
                pelajeRaza = input("Ingrese pelaje: ").lower()
                cuidadosRaza = input("Ingrese cuidados: ").lower()
                energiaRaza = input("Ingrese energía: ").lower()
                esperanzaVidaRaza = input("Ingrese esperanza de vida: ").lower()
                state = input("Ingrese estado: ").lower()

                lista_objetos_raza.append(Raza(tipo_nueva_raza, nombre_nueva_raza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza,
                         energiaRaza, esperanzaVidaRaza, state))

                linea = f"{tipo_nueva_raza};{nombre_nueva_raza};{tamanoRaza};{personalidadRaza};{pelajeRaza};{cuidadosRaza};{energiaRaza};{esperanzaVidaRaza};{state}"

                with open(ruta_completa, 'w', encoding="UTF-8") as f:
                    f.writelines(linea)
                    print(f"{tipo_nueva_raza}_{nombre_nueva_raza}.txt Archivo MODIFICADO")









def main():
    menu_abierto = True
    while menu_abierto :
        op = int(input("Que desea hacer? [1 Buscar raza],[2 modificar raza], [3 agregar], [cualquiera salir]"))

        if op == 1:
            #Buscar Raza
            print("Buscar Raza")
            opcion_tipo_animal = str(input("Tipo de Animal ")).lower()
            opcion_raza_buscar = str(input("Raza a buscar ")).lower()
            buscarRaza(opcion_tipo_animal,opcion_raza_buscar)

        elif op == 2:
            #Modificar Raza
            print("Modificar raza")
            opcion_tipo_animal = str(input("Tipo de Animal ")).lower()
            opcion_raza_buscar = str(input("Raza a buscar ")).lower()
            modificarRaza(opcion_tipo_animal,opcion_raza_buscar)


        elif op == 3:
            nueva_busqueda_tipo = str(input("Tipo de Animal ")).lower()
            nueva_busqueda_raza = str(input("Raza a buscar ")).lower()
            nueva_busquda = buscarRaza(nueva_busqueda_tipo,  nueva_busqueda_raza )
            if nueva_busquda == False:
                agregarRaza(nueva_busqueda_tipo,nueva_busqueda_raza)
            else:
                print(f"La raza {nueva_busqueda_tipo},{nueva_busqueda_raza} ya se encuentra en la lista ")

        else:
            menu_abierto = False






if __name__ == "__main__":
    main()


