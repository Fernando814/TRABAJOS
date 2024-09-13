class Habilidad:
    def __init__(self, nombre, poder):
        self.nombre = nombre
        self.poder = poder

    def __str__(self):
        return f"Habilidad: {self.nombre}, Poder: {self.poder}"
