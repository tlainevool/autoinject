# autoinject
Simple Python Dynamic Injection Framework

Being new to Python after being immersed in the Java world, I was wonder if there were any Dependency Injection Frameworks for setting up components like SPring Does for Java.

For a background on Dependency Injection see Martin Fowler's article: https://martinfowler.com/articles/injection.html

I ran accross these two example in Python: http://code.activestate.com/recipes/413268/ and http://code.activestate.com/recipes/576609/

I was inspired to write my own Constructor based Dynamic Injection.

The first step that needs to be done is to create some components that can be injected into classes:

    from autoinject import components, autoinject

    components['finder'] = movie_components.MontyPythonMovieFinder('monty_python.txt')
    components['printer'] = movie_components.Printer()

Each component has a name (e.g. finder, printer)

AutoInject lets you do inject these components into an object using a decorator like this:
      
    class AnotherMovieLister:
        @autoinject("movie_finder=finder", "printer=printer")
        def __init__(self, movie_finder, printer):
            pass
     

The arguments to the @autoinject decorator are of the form "<argument_name>=<named_component>".

Or you can do injection without modyfing the original class, like this:

    add_autoinject(my_components.MovieLister, 'movie_finder=finder', 'printer=printer')   

Once you have specified your injection, either decorator based, or direct, you can now create your objects:

    movie_lister = AnotherMovieLister()
    
Note that though the original constructor of AnotherMovieLister took in two arguments, you can cnow call the constructor without these argumants, and they will be automatically injected.

You can also override the automatically injected components by specifying keyword arguments in the constructor:

    movie_lister = AnotherMovieLister(printer=FancyPrinter())

See the files in the examples directory for fuller examples
