class Padre:
    def __init__(self):
        self.numero = 12
        print("Constructor clase padre")

    def metodo(self):
        print("Ejecutando método de clase padre")

class Hija(Padre):
    def __init__(self):
        super().__init__()
        print("Constructor clase hija")

    def metHija(self):
        print("Método clase hija")

p = Hija()
# Salida:
# Constructor clase padre
# Constructor clase hija

p.metodo()
# Salida:
# Ejecutando método de clase padre

q = Hija()
# Salida:
# Constructor clase padre
# Constructor clase hija

p.numero = 10
print(p.numero)  # Salida: 10
