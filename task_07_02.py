import random

from string import digits, ascii_letters, punctuation

def password_generator(n):
    lst = lst(digits + ascii_letters + punctuation)
    for i in range(n):
        a = ''.join(random.choice(lst))

    yield a
