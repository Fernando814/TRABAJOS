f = open("persona.txt", "r")
persona = []

while True:
    linea = f.readline().strip()
    if not linea:
            break
    lineas = linea.split(";")
    id = lineas[0]
    nombre = lineas[1]
    fecha = lineas[2]
    apellido = lineas[3]
    d1 = {
    }
    d1["ID"] = id
    d1["Nombre"] = nombre
    d1["Apellidos"] = fecha
    d1["Fecha"] = apellido
    persona.append(d1)
f.close()

for y in persona:
    print(y)
