class Film:
    def __init__(self,name):
        self.name=name
        
    def watch(self):
        print("Bon visionnage !")
        
class FilmCassette(Film):
    def __init__(self, name):
        self.name=name
        self.magnetic_tape=True
    
    def rewind(self):
        print("cest long à rebobiner")
        self.magnetic_tape=True
        

film=Film("2001: l'odyssee de l'espace")
film_cassette = FilmCassette("Bande runner")

print(film_cassette.name)
print(film_cassette.magnetic_tape)
film_cassette.watch()
film_cassette.rewind()