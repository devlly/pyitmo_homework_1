fromcollections import namedtuple


def return_namedtuple(*args1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, tuple):
                trasform = namedtuple('transform', 'args1')
                return transform(*result)
            return result
        return wrapper
    return decorator
