import random

class Movie:
    def __init__(self, title: str, yearOfRelease: str, genre: str, noOFPlays: int):
        self.title = title
        self.yearOfRelease = yearOfRelease
        self.genre = genre
        self.noOfPlays = noOFPlays

    def play(self):
        self.noOfPlays += 1

    def __str__(self):
        return f"{self.title} (" + f"{self.yearOfRelease})"

class Series(Movie):
    def __init__(self, title: str, yearOfRelease: str, genre: str, noOfSeason: int, noOfEpisode: int, noOFPlays: int):
        super().__init__(title, yearOfRelease, genre, noOFPlays)
        self.noOfSeason = noOfSeason
        self.noOfEpisode = noOfEpisode

    def play():
        super().play()

    def __str__(self):
        return f"{self.title} " + "S" + f"{self.noOfSeason:2n}".replace(' ', '0') + "E" + f"{self.noOfEpisode:2n}".replace(' ', '0') 
    

collection = []


movie_1 = Movie("Pulp Fiction", "1994", "Action", 35690)
movie_2 = Movie("Titanic", "1997", "Catastrophic", 96548976)
series_1 = Series("Game of Trone", "2011", "Fantasy", 8, 5, 76968765)
series_2 = Series("House of Cards", "2013", "Drama", 4, 3, 987689)

collection.append(movie_1)
collection.append(movie_2)
collection.append(series_1)
collection.append(series_2)

def get_movies(list: list):
    movies = []
    for i in list:
        if not isinstance(i, Series):
            movies.append(i)
    return sorted(movies, key=lambda i: i.title)

def get_series(list: list):
    serieses = []
    for i in list:
        if not isinstance(i, Series):
            pass
        else:
            serieses.append(i)
    return sorted(serieses, key=lambda i: i.title)

def search(title: str, list: list):
    for i in list:
        if title.casefold() == i.title.casefold():
            return i
        


