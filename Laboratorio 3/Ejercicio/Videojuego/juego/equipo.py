import random

class Equipo:
    def __init__(self, nombre, boost=0):
        self.nombre = nombre
        self.miembros = []
        self.boost = boost  # Boost para aumentar el poder de ataque

    def añadir_miembro(self, personaje):
        self.miembros.append(personaje)

    def listar_miembros(self):
        return [miembro.nombre for miembro in self.miembros]

    def atacar_en_conjunto(self, enemigo):
        print(f"El equipo {self.nombre} ataca en conjunto a {enemigo.nombre}!")
        for miembro in self.miembros:
            miembro.atacar_con_boost(enemigo, self.boost)

    def __str__(self):
        miembros_str = ", ".join(self.listar_miembros())
        return f"Equipo: {self.nombre}, Miembros: {miembros_str}, Boost: {self.boost}"
