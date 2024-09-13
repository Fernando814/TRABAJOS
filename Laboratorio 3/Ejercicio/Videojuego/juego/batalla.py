import random

class Batalla:
    def __init__(self, equipo=None, personaje=None, enemigo=None):
        self.equipo = equipo
        self.personaje = personaje
        self.enemigo = enemigo

    def iniciar_batalla_equipo(self):
        print(f"¡Comienza la batalla entre el equipo {self.equipo.nombre} y {self.enemigo.nombre}!")
        while self.enemigo.salud > 0:
            self.equipo.atacar_en_conjunto(self.enemigo)
            if self.enemigo.salud <= 0:
                print(f"{self.enemigo.nombre} ha sido derrotado por el equipo {self.equipo.nombre}!")
                break

            # Turno del enemigo
            personaje = random.choice(self.equipo.miembros)
            self.enemigo.atacar(personaje)
            if personaje.salud <= 0:
                print(f"{personaje.nombre} ha sido derrotado por {self.enemigo.nombre}!")
                self.equipo.miembros.remove(personaje)
                if not self.equipo.miembros:
                    print(f"Todo el equipo {self.equipo.nombre} ha sido derrotado!")
                    break

    def iniciar_batalla_personaje(self):
        print(f"¡Comienza la batalla entre {self.personaje.nombre} y {self.enemigo.nombre}!")
        while self.personaje.salud > 0 and self.enemigo.salud > 0:
            # Turno del personaje
            self.personaje.atacar(self.enemigo)
            if self.enemigo.salud <= 0:
                print(f"{self.enemigo.nombre} ha sido derrotado!")
                break
            
            # Turno del enemigo
            self.enemigo.atacar(self.personaje)
            if self.personaje.salud <= 0:
                print(f"{self.personaje.nombre} ha sido derrotado!")
                break
