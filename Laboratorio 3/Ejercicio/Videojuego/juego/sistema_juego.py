from .personaje import Personaje
from .enemigo import Enemigo
from .habilidad import Habilidad
from .equipo import Equipo
from .batalla import Batalla

class SistemaJuego:
    def __init__(self):
        self.personajes = []
        self.equipos = []
        self.enemigos = []

    def crear_personaje(self, nombre, rol, salud):
        personaje = Personaje(nombre, rol, salud)
        self.personajes.append(personaje)
        return personaje

    def crear_equipo(self, nombre, boost=0):
        equipo = Equipo(nombre, boost)
        self.equipos.append(equipo)
        return equipo

    def crear_habilidad(self, nombre, poder):
        return Habilidad(nombre, poder)

    def crear_enemigo(self, nombre, fuerza, salud):
        enemigo = Enemigo(nombre, fuerza, salud)
        self.enemigos.append(enemigo)
        return enemigo

    def listar_personajes(self):
        for personaje in self.personajes:
            print(personaje)

    def listar_equipos(self):
        for equipo in self.equipos:
            print(equipo)

    def listar_enemigos(self):
        for enemigo in self.enemigos:
            print(enemigo)

    def menu(self):
        while True:
            print("\n1. Crear personaje")
            print("2. Crear equipo")
            print("3. Crear enemigo")
            print("4. Asignar habilidad a personaje")
            print("5. Asignar boost a equipo")
            print("6. Asignar personaje a equipo")
            print("7. Iniciar batalla (equipo vs enemigo)")
            print("8. Iniciar batalla (personaje vs enemigo)")
            print("9. Salir")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                nombre = input("Nombre del personaje: ")
                rol = input("Rol del personaje: ")
                salud = int(input("Salud del personaje: "))
                personaje = self.crear_personaje(nombre, rol, salud)
                print(f"Personaje {personaje.nombre} creado exitosamente.")

            elif opcion == "2":
                nombre = input("Nombre del equipo: ")
                equipo = self.crear_equipo(nombre)
                print(f"Equipo {equipo.nombre} creado exitosamente.")

            elif opcion == "3":
                nombre = input("Nombre del enemigo: ")
                fuerza = int(input("Fuerza del enemigo: "))
                salud = int(input("Salud del enemigo: "))
                enemigo = self.crear_enemigo(nombre, fuerza, salud)
                print(f"Enemigo {enemigo.nombre} creado exitosamente.")

            elif opcion == "4":
                personaje_nombre = input("Nombre del personaje al que se le asignará la habilidad: ")
                personaje = next((p for p in self.personajes if p.nombre == personaje_nombre), None)
                if personaje:
                    habilidad_nombre = input("Nombre de la habilidad: ")
                    poder = int(input("Poder de la habilidad: "))
                    habilidad = self.crear_habilidad(habilidad_nombre, poder)
                    personaje.agregar_habilidad(habilidad)
                    print(f"Habilidad {habilidad.nombre} asignada a {personaje.nombre}.")
                else:
                    print("Personaje no encontrado.")

            elif opcion == "5":
                equipo_nombre = input("Nombre del equipo: ")
                equipo = next((e for e in self.equipos if e.nombre == equipo_nombre), None)
                if equipo:
                    boost = int(input(f"Ingresa el boost para el equipo {equipo.nombre}: "))
                    equipo.boost = boost
                    print(f"Boost de {boost} asignado al equipo {equipo.nombre}.")
                else:
                    print("Equipo no encontrado.")

            elif opcion == "6":
                personaje_nombre = input("Nombre del personaje: ")
                personaje = next((p for p in self.personajes if p.nombre == personaje_nombre), None)
                equipo_nombre = input("Nombre del equipo: ")
                equipo = next((e for e in self.equipos if e.nombre == equipo_nombre), None)

                if personaje and equipo:
                    personaje.asignar_equipo(equipo)
                    print(f"{personaje.nombre} ha sido asignado al equipo {equipo.nombre}.")
                else:
                    print("Personaje o equipo no encontrado.")

            elif opcion == "7":
                equipo_nombre = input("Nombre del equipo: ")
                equipo = next((e for e in self.equipos if e.nombre == equipo_nombre), None)
                enemigo_nombre = input("Nombre del enemigo: ")
                enemigo = next((en for en in self.enemigos if en.nombre == enemigo_nombre), None)

                if equipo and enemigo:
                    batalla = Batalla(equipo=equipo, enemigo=enemigo)
                    batalla.iniciar_batalla_equipo()
                else:
                    print("Equipo o enemigo no encontrado.")

            elif opcion == "8":
                personaje_nombre = input("Nombre del personaje que va a pelear: ")
                personaje = next((p for p in self.personajes if p.nombre == personaje_nombre), None)
                enemigo_nombre = input("Nombre del enemigo: ")
                enemigo = next((en for en in self.enemigos if en.nombre == enemigo_nombre), None)

                if personaje and enemigo:
                    batalla = Batalla(personaje=personaje, enemigo=enemigo)
                    batalla.iniciar_batalla_personaje()
                else:
                    print("Personaje o enemigo no encontrado.")

            elif opcion == "9":
                break
