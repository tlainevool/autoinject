from functools import wraps

components = dict()


def add_autoinject(injectee, *args):
    """Use this method to inject components into a constructor."""
    injectee.__init__ = inject(injectee.__init__, *args)


def autoinject(*injected_args):
    """Use this method as a decorator to inject components into a constructor."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            add_injectd_args(kwargs, injected_args)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def add_injectd_args(kwargs, injected_args):
    for injected_arg in injected_args:
        (arg_name, component_name) = injected_arg.split('=')
        keys = kwargs.keys()
        if arg_name not in keys:
            kwargs[arg_name] = components[component_name]


def inject(func, *injected_args):
    @wraps(func)
    def wrapper(*args, **kwargs):
        add_injectd_args(kwargs, injected_args)
        return func(*args, **kwargs)

    return wrapper
