import random

class Enemigo:
    def __init__(self, nombre, fuerza, salud):
        self.nombre = nombre
        self.fuerza = fuerza
        self.salud = salud

    def atacar(self, personaje):
        daño = random.randint(1, self.fuerza)
        personaje.salud -= daño
        print(f"{self.nombre} ataca a {personaje.nombre} causando {daño} de daño. Salud restante de {personaje.nombre}: {personaje.salud}")

    def __str__(self):
        return f"Enemigo: {self.nombre}, Fuerza: {self.fuerza}, Salud: {self.salud}"
