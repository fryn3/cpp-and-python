from itertools import islice
from random import random
from time import perf_counter

COUNT = 100000
DATA = list(islice(iter(lambda: (random() - 0.5) * 3.0, None), COUNT))

e = 2.7182818284590452353602874713527

def sinh(x):
    return (1 - (e ** (-2 * x))) / (2 * (e ** -x))

def cosh(x):
    return (1 + (e ** (-2 * x))) / (2 * (e ** -x))

def tanh(x):
    tanh_x = sinh(x) / cosh(x)
    return tanh_x

def sequence_tanh(data):
    '''Applies the hyperbolic tanger function to map all values in
    the sequence to a value between -1.0 and 1.0.
    '''
    result = []
    for x in data:
        result.append(tanh(x))
    return result

def test(fn, name):
    start = perf_counter()

    result = fn(DATA)

    duration = perf_counter() - start
    print('{} took {:.3f} seconds\n\n'.format(name, duration))

    for d in result:
        assert -1 <= d <=1, " incorrect values"

if __name__ == "__main__":
    test(sequence_tanh, 'sequence_tanh')

    test(lambda d: [tanh(x) for x in d], '[tanh(x) for x in d]')
