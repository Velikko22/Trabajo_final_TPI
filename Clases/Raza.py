class Raza:
    def __init__(self, tipoAnimal, nombreRaza, tamanoRaza, personalidadRaza, pelajeRaza, cuidadosRaza, energiaRaza,
                 esperanzaVidaRaza, state):
        self.tipoAnimal = tipoAnimal
        self.nombreRaza = nombreRaza
        self.tamanoRaza = tamanoRaza
        self.personalidadRaza = personalidadRaza
        self.pelajeRaza = pelajeRaza
        self.cuidadosRaza = cuidadosRaza
        self.energiaRaza = energiaRaza
        self.esperanzaVidaRaza = esperanzaVidaRaza
        self.state = state


    def get_tipoAnimal(self):
        return self.tipoAnimal

    def set_tipoAnimal(self, tipoAnimal):
        self.tipoAnimal = tipoAnimal

    def get_nombreRaza(self):
        return self.nombreRaza

    def set_nombreRaza(self, nombreRaza):
        self.nombreRaza = nombreRaza

    def get_tamanoRaza(self):
        return self.tamanoRaza

    def set_tamanoRaza(self, tamanoRaza):
        self.tamanoRaza = tamanoRaza

    def get_personalidadRaza(self):
        return self.personalidadRaza

    def set_personalidadRaza(self, personalidadRaza):
        self.personalidadRaza = personalidadRaza

    def get_pelajeRaza(self):
        return self.pelajeRaza

    def set_pelajeRaza(self, pelajeRaza):
        self.pelajeRaza = pelajeRaza

    def get_cuidadosRaza(self):
        return self.cuidadosRaza

    def set_cuidadosRaza(self, cuidadosRaza):
        self.cuidadosRaza = cuidadosRaza

    def get_energiaRaza(self):
        return self.energiaRaza

    def set_energiaRaza(self, energiaRaza):
        self.energiaRaza = energiaRaza

    def get_esperanzaVidaRaza(self):
        return self.esperanzaVidaRaza

    def set_esperanzaVidaRaza(self, esperanzaVidaRaza):
        self.esperanzaVidaRaza = esperanzaVidaRaza

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state= state


    def __repr__(self):
        return f" {self.tipoAnimal}, {self.nombreRaza}, {self.tamanoRaza}, {self.personalidadRaza}, {self.pelajeRaza}, {self.cuidadosRaza}, " \
               f"{self.energiaRaza}, {self.esperanzaVidaRaza}, {self.state}"
