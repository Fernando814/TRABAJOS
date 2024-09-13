class estudiante:
    def __init__(self, nombre, edad, carrera):
        self._nombre = nombre
        self._edad = edad
        self._carrera = carrera
        self._matricula = False
        self._pension = False

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad

    @property
    def carrera(self):
        return self._carrera

    @carrera.setter
    def carrera(self, nueva_carrera):
        self._carrera = nueva_carrera

