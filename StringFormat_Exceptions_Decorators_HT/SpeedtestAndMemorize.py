from time import perf_counter
from random import randrange
import pickle


def speedtest(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(perf_counter() - start)
        return result
    return inner

@speedtest
def selection_sort(sample: list[int]) -> list[int]:
    sorted_sample = []
    sample = sample.copy()
    for _ in range(len(sample)):
        a = min(sample)
        sorted_sample.append(a)
        sample.remove(a)
    return sorted_sample 

random_list = [randrange(-(10**4), 10**4) for _ in range(10**3)]
print(selection_sort(random_list) == sorted(random_list))


print('---------------')


def memorize(func):
    cache = {}
    def inner(*args, **kwargs):
        hash = pickle.dumps((func.__name__, args, sorted(kwargs.items())))
        if hash not in cache:
            cache[hash] = func(*args, **kwargs)
        return cache[hash]
    return inner

@memorize
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

start = perf_counter()
print(fibonacci(100), perf_counter() - start)
start = perf_counter()
print(fibonacci(101), perf_counter() - start)