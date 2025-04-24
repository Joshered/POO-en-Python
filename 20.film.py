class Film:
    def __init__(self,name):
        self.name=name
        
    def watch(self):
        print("Bon visionnage !")
        
class FilmCassette(Film):
    pass

film=Film("2001: l'odyssee de l'espace")
film_cassette = FilmCassette("Bande runner")

film.name
film.watch()

film_cassette.name
film_cassette.watch()