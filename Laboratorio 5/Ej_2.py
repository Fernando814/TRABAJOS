def carga_datos(archivo):
    personas = []
    empresas = []
    with open(archivo, 'r') as file:
        for linea in file:
            tipo, usuario, contrasena = linea.strip().split(",")
            
            if tipo == 'persona':
                personas.append((usuario, contrasena))
            elif tipo == 'empresa':
                empresas.append((usuario, contrasena))
    return personas, empresas

def verificar_ingreso(lista_usuarios, usuario_ingresado, contrasena_ingresada):
    for usuario, contrasena in lista_usuarios:
        if usuario == usuario_ingresado and contrasena == contrasena_ingresada:
            return True
    return False

personas, empresas = carga_datos('usuarios.txt')

usuario_ingresado = input("Ingrese su nombre de usuario: ")
contrasena_ingresada = input("Ingrese su contraseña: ")

if verificar_ingreso(personas, usuario_ingresado, contrasena_ingresada):
    print("Ingreso exitoso como persona.")
elif verificar_ingreso(empresas, usuario_ingresado, contrasena_ingresada):
    print("Ingreso exitoso como empresa.")

else:
    print("Usuario o contraseña incorrectos.")
