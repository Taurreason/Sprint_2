class Movies:

    def __init__(self, movie):
        self.movies = []
        self.movie = movie

    def add_movie(self, movie):
        return self.movies.append(movie)


class Comedy(Movies):

    def __init__(self, movie):
        super().__init__(movie)

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Комедии: {self.movies}'


class Drama(Movies):

    def __init__(self, movie):
        super().__init__(movie)

    def add_movie(self, movie):
        self.movies.append(movie)
        return f'Драмы: {self.movies}'


film_comedy = Comedy('Большой куш')
film_drama = Drama('Оружейный барон')
print(film_comedy.add_movie('Большой куш'))
print(film_drama.add_movie('Оружейный барон'))