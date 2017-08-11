# autoinject

Simple Python Dynamic Injection Framework

Being new to Python after being immersed in the Java world, I was wonder if there were any Dependency Injection Frameworks for setting up components like Spring Does for Java.

For a background on Dependency Injection see Martin Fowler's article: https://martinfowler.com/articles/injection.html

I ran accross these two example in Python: http://code.activestate.com/recipes/413268/ and http://code.activestate.com/recipes/576609/

I was inspired to write my own Constructor based Dynamic Injection.

If you are wondering about how to create decorators, this [amazing Stack Overflow Answer](https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators#answer-1594484) is a great resource.

## Basic Usage

The first step that needs to be done is to create some components that can be injected into classes:

    from autoinject import components, autoinject, add_autoinject
        
    components['finder'] = movie_components.MontyPythonMovieFinder('monty_python.txt')
    components['printer'] = movie_components.Printer()

Each component has a name (e.g. finder, printer)

AutoInject lets you do inject these named components into an object using a decorator like this:
      
    class MovieLister:
        @autoinject("movie_finder=finder", "printer=printer")
        def __init__(self, movie_finder, printer):
            pass
     
The arguments to the @autoinject decorator are of the form "<argument_name>=<named_component>".

Once you have specified your injection, either decorator based, or direct, you can now create your objects:

    movie_lister = MovieLister()
    
Note that though the original constructor of MovieLister took in two arguments, you can now call the constructor without these argumants, and they will be automatically injected.

You can also do injection without modyfing the original class, like this:

    class AnotherMovieLister:
        
        def __init__(self, movie_finder, printer):
            pass
     
    add_autoinject(AnotherMovieLister, 'movie_finder=finder', 'printer=printer')   


You can also override the automatically injected components by specifying keyword arguments in the constructor:

    movie_lister = AnotherMovieLister(printer=FancyPrinter())

See the files in the examples directory for more complete examples

## Ideas for Enhancements
- Get rid of the need to have argname=component name lsist - allow matching by position or match component names to argument names if they are the same.
- Allow for component naming and injection in on step, e.g. build_componet('name', Bar, 'some_arg=some_component) 
