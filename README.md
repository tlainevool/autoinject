# autoinject
Simple Python Dynamic Injection Framework

Being new to Python after being immersed in the Java world, I was wonder if there were any Dependency Injection Frameworks for setting up components like SPring Does for Java.

For a background on Dependency Injection see Martin Fowler's article: https://martinfowler.com/articles/injection.html

I ran accross these two example in Python: http://code.activestate.com/recipes/413268/ and http://code.activestate.com/recipes/576609/

I was inspired to write my own Constructor based Dynamic Injection.

AutoInject lets you do decorator based injection like this:
  
    from autoinject import components, autoinject
      
    components['finder'] = movie_components.MontyPythonMovieFinder('monty_python.txt')
    components['printer'] = movie_components.Printer()
      
    class AnotherMovieLister:
        @autoinject("movie_finder=finder", "printer=printer")
        def __init__(self, movie_finder, printer):
            pass
     

Or you can do injection without modyfing the original class, like this:
    from autoinject import components, add_autoinject
    
    components['finder'] = my_components.MontyPythonMovieFinder()
    components['printer'] = my_components.Printer()
      
    add_autoinject(my_components.MovieLister, 'movie_finder=finder', 'printer=printer')   
    
See thefiles in the examples directory for fuller examples
