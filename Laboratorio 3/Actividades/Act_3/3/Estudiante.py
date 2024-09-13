class estudiante:
    numero_estudiantes = 0

    def __new__(cls, *args):
        print("Llamando a __new__")
        instancia = super(estudiante, cls).__new__(cls)
        return instancia

    def __init__(self, nombre, edad, carrera):
        print("Llamando a __init__")
        self._nombre = nombre
        self._edad = edad
        self._carrera = carrera
        self._matricula = False
        self._pension = False
        estudiante.numero_estudiantes += 1

    def __del__(self):
        print("El estudiante", self._nombre, "está siendo eliminado")
        estudiante.numero_estudiantes -= 1

    @staticmethod
    def contar_estudiantes():
        print("Número total de estudiantes:", estudiante.numero_estudiantes)

