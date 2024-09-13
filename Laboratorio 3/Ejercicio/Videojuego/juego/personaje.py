import random
from .habilidad import Habilidad
from .equipo import Equipo

class Personaje:
    def __init__(self, nombre, rol, salud):
        self.nombre = nombre
        self.rol = rol
        self.salud = salud
        self.equipo = None
        self.habilidades = []

    def asignar_equipo(self, equipo: Equipo):
        self.equipo = equipo
        equipo.añadir_miembro(self)

    def agregar_habilidad(self, habilidad: Habilidad):
        self.habilidades.append(habilidad)

    def atacar(self, enemigo):
        if self.habilidades:
            habilidad = random.choice(self.habilidades)
            print(f"{self.nombre} usa {habilidad.nombre}!")
            enemigo.salud -= habilidad.poder
            print(f"{enemigo.nombre} recibe {habilidad.poder} de daño. Salud restante: {enemigo.salud}")
        else:
            print(f"{self.nombre} no tiene habilidades asignadas para atacar.")

    def atacar_con_boost(self, enemigo, boost):
        if self.habilidades:
            habilidad = random.choice(self.habilidades)
            poder_con_boost = habilidad.poder + boost
            print(f"{self.nombre} usa {habilidad.nombre} con boost! (+{boost})")
            enemigo.salud -= poder_con_boost
            print(f"{enemigo.nombre} recibe {poder_con_boost} de daño. Salud restante: {enemigo.salud}")
        else:
            print(f"{self.nombre} no tiene habilidades asignadas para atacar.")

    def __str__(self):
        habilidades_str = ", ".join([str(hab) for hab in self.habilidades])
        equipo_str = self.equipo.nombre if self.equipo else "Sin equipo"
        return f"Personaje: {self.nombre}, Rol: {self.rol}, Salud: {self.salud}, Equipo: {equipo_str}, Habilidades: {habilidades_str}"
