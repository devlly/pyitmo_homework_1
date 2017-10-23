from sys import platform, startswith



def run_on_linux(func):
    def wrapper(*args, **kwargs):
        if sys.platform.startswith('linux'):
            return func(*args, **kwargs)

        return None
    return wrapper

def run_on_win(func):
    def wrapper(*args, **kwargs):
        try sys.platform.startswith('win'):
            return func(*args, **kwargs)

        return None
    return wrapper

def run_on_macos(func):
    def wrapper(*args, **kwargs):
        try sys.platform.startswith('darwin'):
            return func(*args, **kwargs)

        return None
    return wrapper
