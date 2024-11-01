from datetime import datetime

class Usuario:
    def __init__(self, nombre, contraseña_final):
        self.nom = nombre
        self.contra = contraseña_final
        self.fecha_ingreso = ""

    def ingresar(self, contraseña_web):
        if contraseña_web == self.contra:
            self.fecha_ingreso = datetime.now()
            print(f"Ingreso exitoso a las {self.fecha_ingreso}")
            return True
        else:
            print("Contraseña incorrecta")
            return False

class Persona(Usuario):
    def __init__(self, nombre, dni, contraseña):
        super().__init__(nombre, contraseña)
        self.dni = dni

    def ingresar(self, dni, contraseña):
        if dni == self.dni:
            return super().ingresar(contraseña)
        else:
            print("DNI incorrecto")
            return False
class Empresa(Usuario):

    def __init__(self, nombre, ruc, contrasena):
        super().__init__(nombre, contrasena)
        self.ruc = ruc

    def ingresar(self, ruc, contrasena):
        if ruc == self.ruc:
            return super().ingresar(contrasena)
        else:
            print("RUC incorrecto")
            return False
        
persona = Persona("pedro Suarez", "12", "rtfghy")
empresa = Empresa("Toyota", "123212654387", "wqapxw")

persona.ingresar("12", "rtfghy")
empresa.ingresar("123212654387", "wqapxw")
