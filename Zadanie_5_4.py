import random
import datetime

class Movie:
    def __init__(self, title: str, year_of_release: str, genre: str, no_of_plays = 0):
        self.__title = title
        self.__year_of_release = year_of_release
        self.__genre = genre
        self.__no_of_plays = no_of_plays

    @property
    def title_pr(self):
        return self.__title    

    @property
    def year_of_release_pr(self):
        return self.__year_of_release

    @property
    def no_of_plays_pr(self):
        return self.__no_of_plays
    
    @no_of_plays_pr.setter
    def no_of_plays_pr(self, new_no_of_plays: int):
        self.__no_of_plays += new_no_of_plays

    @property
    def play(self):
        self.__no_of_plays += 1

    def __str__(self):
        return f"{self.title_pr} (" + f"{self.year_of_release_pr})"

class Series(Movie):
    def __init__(self, title: str, year_of_release: str, genre: str, no_of_season = 1, no_of_episode = 1, no_of_plays = 0):
        super().__init__(title, year_of_release, genre, no_of_plays)
        self.__no_of_season = no_of_season
        self.__no_of_episode = no_of_episode
        
    @property
    def no_of_season_pr(self):
        return self.__no_of_season
    
    @no_of_season_pr.setter
    def no_of_season_pr(self, new_no):
        self.__no_of_season = new_no
    
    @property
    def no_of_episode_pr(self):
        return self.__no_of_episode
    
    @no_of_episode_pr.setter
    def no_of_episode_pr(self, new_no):
        self.__no_of_episode = new_no

    def __str__(self):
        return f"{self.title_pr} " + "S" + f"{self.no_of_season_pr:2n}".replace(' ', '0') + "E" + f"{self.no_of_episode_pr:2n}".replace(' ', '0') 
    

class Methods:
    def __init__(self):
        pass
    
    @staticmethod
    def get_movies(list: list):
        movies = []
        for i in list:
            if type(i) is Movie:
                movies.append(i)
        return sorted(movies, key=lambda i: i.title_pr)

    @staticmethod
    def get_series(list: list):
        serieses = []
        for i in list:
            if type(i) is Series:
                serieses.append(i)
        return sorted(serieses, key=lambda i: i.title_pr)

    @staticmethod
    def search(title: str, list: list):
        for i in list:
            if title.casefold() == i.title_pr.casefold():
                return i
     
    @staticmethod
    def generate_views(list: list):
        item = random.choice(list)
        item.no_of_plays_pr = random.randint(0, 101)

    @staticmethod
    def genetare_views_x10(list: list):
        for i in range(10):
            Methods.generate_views(list)

    @staticmethod
    def top_titles(list: list, content_type: str, quantity: int):
        if content_type.casefold() == "movie":
            movies = sorted(Methods.get_movies(list), key=lambda movie: movie.no_of_plays_pr, reverse=True)
            top_movies = movies[:quantity]
            return top_movies
        elif content_type.casefold() == "series":
            episodes = sorted(Methods.get_series(list), key=lambda episode: episode.no_of_plays_pr, reverse=True)
            top_episodes = episodes[:quantity]
            return top_episodes
        else:
            print("Only types 'Movie' and 'Series' are allowed")

    @staticmethod
    def add_full_season(title: str, year_of_release: str, genre: str, no_of_seasons=1, no_of_episodes=1, no_of_plays=0):
        season_list = []
        for e in range(no_of_episodes):  
            season_list.append(Series(title, year_of_release, genre, no_of_seasons, e+1, no_of_plays))
        return season_list

print("Biblioteka filmów")

collection = []

movie_1 = Movie("Pulp Fiction", "1994", "Action")
movie_2 = Movie("Titanic", "1997", "Catastrophic")
movie_3 = Movie("The Shawshank Redemption", "1994", "Drama")
movie_4 = Movie("Intouchables", "2011", "Biographic")
movie_5 = Movie("The Green Mile", "1999", "Drama")

collection.append(movie_1)
collection.append(movie_2)
collection.append(movie_3)
collection.append(movie_4)
collection.append(movie_5)

series_1 = Methods.add_full_season("Game of Trone", "2011", "Fantasy", 1, 10)
series_2 = Methods.add_full_season("House of Cards", "2013", "Drama", 1, 10)

collection =  collection + series_1 + series_2

for i in range(101):
    Methods.genetare_views_x10(collection)

top_episedes = Methods.top_titles(collection, "series", 3)
top_movies = Methods.top_titles(collection, "movie", 3)

print(f"Najpopularniejsze odcinki seriali dnia {datetime.date.today().strftime('%d.%m.%Y')} to:")

for e in top_episedes:
    print(e)

print(f"Najpopularniejsze filmy dnia {datetime.date.today().strftime('%d.%m.%Y')} to:")

for m in top_movies:
    print(m)