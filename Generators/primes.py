from math import sqrt
from time import perf_counter


def primes_gen():
    i = 1
    while True:
        if i == 1:
            yield 2
        i += 2
        for j in range(3, int(sqrt(i)) + 2, 2):
            if not i % j:
                break
        else:
            yield i

def primes_genn():
    i = 1
    previous = [3]
    while True:
        if i == 1:
            yield 2
        i += 2
        for j in previous[1:]:
            if not i % j:
                break
        else:
            previous.append(i)
            yield i

p1 = primes_gen()
p2 = primes_genn()
for _ in range(30):
    print(next(p1), next(p2))

primes = primes_gen()
t = perf_counter()
for _ in range(5000):
    next(primes)
t1 = perf_counter() - t

primes2 = primes_genn()
t = perf_counter()
for _ in range(5000):
    next(primes2)    
t2 = perf_counter() - t

print(t1, t2)
print(min((t1, t2)))
print(t2/t1)