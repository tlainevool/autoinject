from autoinject import components, add_autoinject
import examples.movie_components as my_components

#First do the assembly
components['mp_file_name'] = 'monty_python.txt'
add_autoinject(my_components.MontyPythonMovieFinder, 'file_name=mp_file_name')

components['finder'] = my_components.MontyPythonMovieFinder()


components['printer'] = my_components.Printer()

add_autoinject(my_components.MovieLister, 'movie_finder=finder', 'printer=printer')


# Now we can use the classes that we have autoinjected components into, without specifying the components
print('Plain:')
list = my_components.MovieLister()
list.movies_directed_by('Terry Jones')



# We can also send in some (or all) of the arguments via keyword arguments, to override the injected ones
print('\nNow Fancy:')
fancy_list = my_components.MovieLister(printer=my_components.FancyPrinter())
fancy_list.movies_directed_by('Ian MacNaughton')
