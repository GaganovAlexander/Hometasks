from random import randrange
import time
from SomePreviousAlgorithms import *
from BinaryInsertSort import *
from merge_sort import *


MAX_RANGE = 10**4    
NUM_OF_ELEMENTS = 10**4 + 3


def check(sample: list[int], bild_in_function, *functions):
    start_time = time.perf_counter()
    bild_in_result = bild_in_function(sample)
    print(f'Bild in function: \033[34m{time.perf_counter() - start_time} \033[0mSeconds')
    for func in functions:
        start_time = time.perf_counter()
        our_result = func(sample)
        print(f'\033[0m{func.__name__}: \033[34m{round(time.perf_counter() - start_time, 7)} \033[0mSeconds')
        if bild_in_result == our_result:
            print(f'\033[32mTrue\033[0m')
        else:
            print(f'\033[31mFalse\033[0m')

def check_with_method(sample: list[int], variations: list[int], func):
    total_time_bi = 0
    total_time_of = 0

    for i in variations:
        start_time = time.perf_counter()
        try:
            bild_in_result = sample.index(i)
        except:
            bild_in_result = None
        total_time_bi += time.perf_counter() - start_time

        start_time = time.perf_counter()
        our_result = func(sample, i)
        total_time_of += time.perf_counter() - start_time

        if bild_in_result != our_result:
            print(our_result, bild_in_result)
    print(f'Bild in method: {total_time_bi} Seconds')
    print(f'{func.__name__}: {total_time_of} Seconds')

random_sample = [randrange(-MAX_RANGE, MAX_RANGE) for _ in range(NUM_OF_ELEMENTS)]
#check_with_method(sorted(random_sample), [randrange(-1000, 1000) for _ in range(100)], binary_search)
check(random_sample, sorted, merge_sort, binary_insert_sort, merge_sort_without_rec)
