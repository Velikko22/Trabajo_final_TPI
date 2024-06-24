class ViewRaza:
    def mostrarOpcionesMenuRaza(self):
        print("===========")
        print("[1] Mostrar Todas las Razas \n"
              "[2] Buscar Raza y Mostrar \n"
              "[3] Modificar Raza \n"
              "[4] Agregar Raza \n"
              "[5] Eliminar Raza \n"
              "[6] Mostrar todas las Mascotas \n"
              )


    def mensajeRazaNoencontrada(self):
        print("RAZA NO ENCONTRADA, DEBE AGREGARLA ")

    def mostrarPantallaRazasDisponibles(self,lista):
        for animal in lista:
            if animal.state == 1:
                print(f"Especie: {animal.tipoAnimal} , Nombre Raza: {animal.nombreRaza}")

    def MostrarRazaEliminada(self):
        print("La raza se encuentra INACTIVA o Eliminada ")


    def mensajeRazaEncontrada(self):
        print("Raza ENCONTRADA! ")

