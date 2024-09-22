class Individuo:
    def __init__(self, nombre, apellido, edad):
        # Inicializa el nombre, apellido y edad del individuo
        self.nombre = nombre
        self.apellido = apellido
        self.anios = edad

    def __str__(self):
        # Retorna una cadena que describe al individuo
        return f"{self.nombre} {self.apellido}, {self.anios} años"


class Empleado:
    def __init__(self, organizacion):
        # Inicializamos la organización o empresa a la que pertenece el empleado
        self.organizacion = organizacion

    def __str__(self):
        # Retornamos una cadena que describe al empleado
        return f"Empleado de {self.organizacion}"


class Mantenimiento(Individuo, Empleado):
    def __init__(self, nombre, apellido, edad, organizacion):
        # Inicializamos los atributos de Individuo y Empleado
        Individuo.__init__(self, nombre, apellido, edad)
        Empleado.__init__(self, organizacion)

    def __str__(self):
        # Retornamos una cadena que describe al personal de mantenimiento
        return f"{self.nombre} {self.apellido}, {self.anios} años, Personal de mantenimiento de {self.organizacion}"


# Ejemplo de uso:
persona = Mantenimiento("Juan", "Pérez", 30, "TechCorp")
print(persona)
# Salida: Juan Pérez, 30 años, Personal de mantenimiento de TechCorp
