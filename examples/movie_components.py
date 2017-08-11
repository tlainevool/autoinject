"""Define some components that can be injected"""


class Printer():
    def print(self, s):
        print(s)


class FancyPrinter():
    def print(self, s):
        print('--> ' + s)


class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director


class MovieLister:
    def __init__(self, movie_finder, printer):
        self.movie_finder = movie_finder
        self.printer = printer

    def movies_directed_by(self, director):
        all_movies = self.movie_finder.find_all()
        for movie in all_movies:
            if movie.director == director:
                self.printer.print(movie.title)


class MontyPythonMovieFinder:
    def __init__(self, file_name):
        self.file_name = file_name
        # pretend this is loaded from a file
        self.movies = [
            Movie('And Now for Something Completely Different', 'Ian MacNaughton'),
            Movie('Monty Python\'s Life of Brian', "Terry Jones")
        ]

    def find_all(self):
        return self.movies
