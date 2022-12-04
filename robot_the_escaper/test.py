from slow_variation import slow_var
from fast_variation import fast_var
from time import perf_counter
from random import choice, randrange


map_ = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 2, 1, 0],
        [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


for i in slow_var(map_):
    print(i)

print('-----------------')

for i in fast_var(map_):
    print(i)

t11 = 0
t22 = 0
ittr = 0
for i in range(200):
    map_ = [[choice((0, 1)) for _ in range(100)] for _ in range(40)]
    map_[randrange(20)][randrange(100)] = 2

    if ittr % 2:
        t2 = perf_counter()
        map2 = fast_var(map_)
        t22 += perf_counter() - t2

        t1 = perf_counter()
        map1 = slow_var(map_)
        t11 += perf_counter() - t1
    else:
        t1 = perf_counter()
        map1 = slow_var(map_)
        t11 += perf_counter() - t1

        t2 = perf_counter()
        map2 = fast_var(map_)
        t22 += perf_counter() - t2

    if map1 != map2:
        for i in map1:
            print(i)

        print('-----------------')

        for i in map2:
            print(i)
    ittr += 1

print(f'Slow func time: {t11}; fast func time: {t22}')
print(f'Ration slower/faster: {t11/t22}')


