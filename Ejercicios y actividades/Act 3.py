class Delfin:
    def nadar(self):                        # Método para indicar que el delfín está nadando  
        print("Daniel, el delfín, está nadando.")             
    
    def nadarHaciaAtras(self):              # Método para indicar que el delfín no puede nadar hacia atrás
        print("Daniel no puede nadar hacia atrás, pero puede sumergirse hacia atrás.")
    
    def esqueleto(self):                    # Método para describir el tipo de esqueleto del delfín
        print("El esqueleto de Daniel está hecho de hueso.")

class Ballena:
    def nadar(self):                        # Método para indicar que la ballena está nadando
        print("Destiny, la ballena, está nadando.")
    
    def nadarHaciaAtras(self):              # Método para indicar que la ballena puede nadar hacia atrás
        print("Destiny puede nadar hacia atrás.")
    
    def esqueleto(self):                    # Método para describir el tipo de esqueleto de la ballena
        print("El esqueleto de Destiny está hecho de hueso.")

Daniel = Delfin()                           # Creación de instancias de la clase Delfin y Ballena
Destiny = Ballena()

nadadores = [Daniel, Destiny]                 # Lista de objetos que incluye al delfín y la ballena

for x in nadadores:                           # Bucle para ejecutar los métodos de cada objeto en la lista
    print("Nadando:")
    x.nadar()                       # Llama al método nadar
    print("Nadando hacia atrás:")
    x.nadarHaciaAtras()             # Llama al método nadarHaciaAtras
    print("Esqueleto:")
    x.esqueleto()                   # Llama al método esqueleto
    print("---")
