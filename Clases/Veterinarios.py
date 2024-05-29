from Persona import Personas

class veterinario(Personas):
    
    def __init__(self,cargo):
        self.cargo = cargo
    
    def __str__(self):
        return self.cargo
    
    def __repr__(self):
        return