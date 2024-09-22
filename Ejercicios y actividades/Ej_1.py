class Persona:
    def __init__(self, id, nombre, apellido):
        self._id = id  # encapsulamiento usando prefijo "_"
        self._nombre = nombre
        self._apellido = apellido

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, Apellido: {self._apellido}"

class EstudianteIS(Persona):
    def __init__(self, id, nombre, apellido, semestre):
        super().__init__(id, nombre, apellido)
        self._semestre = semestre

    def get_semestre(self):
        return self._semestre

    def __str__(self):
        return f"{super().__str__()}, Semestre: {self._semestre}"

class Cliente(Persona):
    def __init__(self, id, nombre, apellido, direccion, codigo, estado):
        super().__init__(id, nombre, apellido)
        self._direccion = direccion
        self._codigo = codigo
        self._estado = estado

    def get_direccion(self):
        return self._direccion

    def get_codigo(self):
        return self._codigo

    def get_estado(self):
        return self._estado

    def __str__(self):
        return f"{super().__str__()}, Dirección: {self._direccion}, Código: {self._codigo}, Estado: {self._estado}"

class Empleado(Persona):
    def __init__(self, id, nombre, apellido, fecha_ingreso, cargo, sueldo=2500):
        super().__init__(id, nombre, apellido)
        self._fecha_ingreso = fecha_ingreso
        self._cargo = cargo
        self._sueldo = sueldo

    def get_fecha_ingreso(self):
        return self._fecha_ingreso

    def get_cargo(self):
        return self._cargo

    def get_sueldo(self):
        return self._sueldo

    def __str__(self):
        return f"{super().__str__()}, Fecha de Ingreso: {self._fecha_ingreso}, Cargo: {self._cargo}, Sueldo: {self._sueldo}"

    def __del__(self):
        print(f"Empleado {self._nombre} {self._apellido} eliminado")

# Crear objetos de cada clase
estudiante = EstudianteIS("123456", "Juan", "Pérez", 5)
cliente = Cliente("987654", "María", "González", "Calle 123", "12345", "Activo")
empleado = Empleado("111111", "Pedro", "Rodríguez", "2020-01-01", "Ingeniero", 5000)

# Imprimir información de los objetos
print(estudiante)
print(cliente)
print(empleado)

# Eliminar empleado
del empleado
