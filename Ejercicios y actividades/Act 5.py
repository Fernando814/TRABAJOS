class Delfin:
    def nadar(self):
        print("El delfín está nadando.")

class Ballena:
    def nadar(self):
        print("La ballena está nadando.")

def enElPacifico(animal):
    animal.nadar()

daniel = Delfin()
bella = Ballena()

enElPacifico(daniel)
enElPacifico(bella)
