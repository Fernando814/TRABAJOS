class Delfin:
    # Método para indicar que el delfín está nadando
    def nadar(self):
        print("Daniel, el delfín, está nadando.")
    
    # Método para indicar que el delfín no puede nadar hacia atrás
    def nadarHaciaAtras(self):
        print("Daniel no puede nadar hacia atrás, pero puede sumergirse hacia atrás.")
    
    # Método para describir el tipo de esqueleto del delfín
    def esqueleto(self):
        print("El esqueleto de Daniel está hecho de hueso.")

class Ballena:
    # Método para indicar que la ballena está nadando
    def nadar(self):
        print("Destiny, la ballena, está nadando.")
    
    # Método para indicar que la ballena puede nadar hacia atrás
    def nadarHaciaAtras(self):
        print("Destiny puede nadar hacia atrás.")
    
    # Método para describir el tipo de esqueleto de la ballena
    def esqueleto(self):
        print("El esqueleto de Destiny está hecho de hueso.")

# Creación de instancias de la clase Delfin y Ballena
Daniel = Delfin()
Destiny = Ballena()

# Bucle que recorre los objetos delfín y ballena
for peces in (Daniel, Destiny):
    peces.nadar()  # Llama al método nadar
    peces.nadarHaciaAtras()  # Llama al método nadarHaciaAtras
    peces.esqueleto()  # Llama al método esqueleto
