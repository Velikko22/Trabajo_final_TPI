import datetime
class FichaMedica:
    def __init__(self,identificador):
        self.identificador = identificador
        self.fecha = datetime.datetime.today()

    def __repr__(self):
        return f"{self.identificador},{self.fecha}"


asd = FichaMedica(1)
print(asd.fecha)