from Estudiante import estudiante  # Importa la clase estudiante

# Crea una instancia de la clase estudiante
Estudiante2 = estudiante("", 20, "Ingeniería de Sistemas")

# Intenta cambiar la edad a -1
Estudiante2.edad = -1
print(Estudiante2.edad)  # Debería imprimir 20, porque -1 no es válido

# Cambia el nombre y la carrera
Estudiante2.nombre = "Jose"
print(Estudiante2.nombre)  # Imprime "Jose"

Estudiante2.carrera = "Psicología"
print(Estudiante2.carrera)  # Imprime "Psicología"
