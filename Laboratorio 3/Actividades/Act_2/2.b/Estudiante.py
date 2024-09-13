class estudiante:
    numero_estudiantes = 0

    def __init__(self, nombre, edad, carrera):
        self._nombre = nombre
        self._edad = edad
        self._carrera = carrera
        self._matricula = False
        self._pension = False
        estudiante.numero_estudiantes += 1

    @classmethod
    def contar_estudiantes(cls):
        return "Número total de estudiantes:", cls.numero_estudiantes
