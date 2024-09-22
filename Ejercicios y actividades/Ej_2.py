from datetime import datetime, timedelta
import random

class Vehiculo:
    def __init__(self, capacidad):
        self.capacidad = capacidad

class Avion(Vehiculo):
    def __init__(self, capacidad):
        super().__init__(capacidad)

class Bus(Vehiculo):
    def __init__(self, capacidad):
        super().__init__(capacidad)

class Pasajero:
    def __init__(self, nombre):
        self.nombre = nombre

class Viaje:
    def __init__(self, codigo_viaje, origen, destino, fecha, capacidad, vehiculo):
        self.codigo_viaje = codigo_viaje
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.capacidad = capacidad
        self.vehiculo = vehiculo
        self.reservas = []

    def realizar_reserva(self, pasajero):
        if len(self.reservas) < self.capacidad:
            # Verificamos si falta más de 1 hora para el viaje
            tiempo_restante = self.fecha - datetime.now()
            if tiempo_restante > timedelta(hours=1):
                self.reservas.append(pasajero)
                print("Reserva realizada con éxito")
            else:
                print("No se puede realizar la reserva. Falta menos de 1 hora para el viaje")
        else:
            print("No se puede realizar la reserva. Capacidad máxima alcanzada")

    def cancelar_reserva(self, pasajero):
        if pasajero in self.reservas:
            self.reservas.remove(pasajero)
            print("Reserva cancelada con éxito")
        else:
            print("No se encontró la reserva para cancelarla")

class Reservas:
    def __init__(self):
        self.viajes = []

    def agregar_viaje(self, viaje):
        self.viajes.append(viaje)

    def mostrar_disponibilidad(self):
        for viaje in self.viajes:
            asientos_disponibles = viaje.capacidad - len(viaje.reservas)
            print(f"Viaje {viaje.codigo_viaje}: {asientos_disponibles} asientos disponibles")

    def generar_viajes_aleatorios(self):
        ciudades = ["Ciudad A", "Ciudad B", "Ciudad C", "Ciudad D", "Ciudad E"]
        vehiculos = [Avion(200), Bus(50)]
        for i in range(5):  # Genera 5 viajes aleatorios
            origen = random.choice(ciudades)
            destino = random.choice([c for c in ciudades if c != origen])
            fecha = datetime.now() + timedelta(days=random.randint(1, 10), hours=random.randint(0, 23))
            vehiculo = random.choice(vehiculos)
            codigo_viaje = f"V{i+1}"
            viaje = Viaje(codigo_viaje, origen, destino, fecha, vehiculo.capacidad, vehiculo)
            self.agregar_viaje(viaje)

class Menu:
    def __init__(self, reservas):
        self.reservas = reservas

    def mostrar_menu(self):
        print("Menú:")
        print("1. Reservar un viaje")
        print("2. Ver disponibilidad de viajes")
        print("3. Cancelar un viaje")
        print("4. Salir")

    def ejecutar_menu(self):
        while True:
            self.mostrar_menu()
            opcion = input("Ingrese una opción: ")
            if opcion == "1":
                codigo_viaje = input("Ingrese el código de viaje: ")
                nombre_pasajero = input("Ingrese su nombre: ")
                pasajero = Pasajero(nombre_pasajero)
                for viaje in self.reservas.viajes:
                    if viaje.codigo_viaje == codigo_viaje:
                        viaje.realizar_reserva(pasajero)
                        break
                else:
                    print("No se encontró el viaje para realizar la reserva")
            elif opcion == "2":
                self.reservas.mostrar_disponibilidad()
            elif opcion == "3":
                codigo_viaje = input("Ingrese el código de viaje: ")
                nombre_pasajero = input("Ingrese su nombre: ")
                pasajero = Pasajero(nombre_pasajero)
                for viaje in self.reservas.viajes:
                    if viaje.codigo_viaje == codigo_viaje:
                        viaje.cancelar_reserva(pasajero)
                        break
                else:
                    print("No se encontró el viaje para cancelar la reserva")
            elif opcion == "4":
                return
            else:
                print("Opción inválida. Intente nuevamente")

# Inicializamos el sistema de reservas con viajes aleatorios
reservas = Reservas()
reservas.generar_viajes_aleatorios()

menu = Menu(reservas)
menu.ejecutar_menu()
