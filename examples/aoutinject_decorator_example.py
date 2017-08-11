import examples.movie_components as movie_components
from autoinject import components, autoinject

# We can use a decorator to inject named components

# First do the component registration

components['finder'] = movie_components.MontyPythonMovieFinder('monty_python.txt')
components['printer'] = movie_components.Printer()


class AnotherMovieLister:
    @autoinject("movie_finder=finder", "printer=printer")
    def __init__(self, movie_finder, printer):
        self.movie_finder = movie_finder
        self.printer = printer

    def movies_directed_by(self, director):
        all_movies = self.movie_finder.find_all()
        for movie in all_movies:
            if movie.director == director:
                self.printer.print(movie.title)

# Now we can use the classes that we have autoinjected components into, without specifying the components
print('Plain:')
list = AnotherMovieLister()
list.movies_directed_by('Terry Jones')

# We can use keyword arguments to overridr the injected compnents
print('\nFancy:')
list = AnotherMovieLister(printer=movie_components.FancyPrinter())
list.movies_directed_by('Ian MacNaughton')

