import pickle

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance

    def __str__(self):
        return f"Nombre: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}, Alcance: {self.alcance}"

class Gestor:
    def __init__(self):
        self.personajes = self.cargar_personajes()

    def cargar_personajes(self):
        try:
            with open('personajes.pckl', 'rb') as fichero:
                personajes = pickle.load(fichero)
            return personajes
        except:
            return {}

    def guardar_personajes(self):
        with open('personajes.pckl', 'wb') as fichero:
            pickle.dump(self.personajes, fichero)

    def agregar_personaje(self, personaje):
        if personaje.nombre in self.personajes:
            print("El personaje ya existe en el Gestor.")
        else:
            self.personajes[personaje.nombre] = personaje
            self.guardar_personajes()
            print("Personaje agregado con éxito.")

    def mostrar_personajes(self):
        for personaje in self.personajes.values():
            print(personaje)

    def borrar_personaje(self, nombre):
        if nombre in self.personajes:
            del self.personajes[nombre]
            self.guardar_personajes()
            print("Personaje borrado con éxito.")
        else:
            print("El personaje no existe en el Gestor.")

gestor = Gestor()
gestor.agregar_personaje(Personaje("Arquero", 2, 4, 1, 8))
gestor.agregar_personaje(Personaje("Guerrero", 2, 4, 2, 4))
gestor.agregar_personaje(Personaje("Caballero", 4, 4, 4, 2))
print("\nPersonajes del Gestor:")
gestor.mostrar_personajes()

gestor.borrar_personaje("Arquero")
print("\nPersonajes del Gestor después de borrar al Arquero:")
gestor.mostrar_personajes()
