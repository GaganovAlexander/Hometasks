from random import randrange
import time
from SomePreviousAlgorithms import *
from BinaryInsertSort import *


MAX_RANGE = 10**4    
NUM_OF_ELEMENTS = 10**4


def check(sample: list[int], bild_in_function, *functions):
    start_time = time.time()
    bild_in_result = bild_in_function(sample)
    print(f'Bild in function: {time.time() - start_time} Seconds')
    for func in functions:
        start_time = time.time()
        our_result = func(sample)
        print(f'{func.__name__}: {round(time.time() - start_time, 7)} Seconds')
        if bild_in_result == our_result:
            print(True)
        else:
            print(False)

def check_with_method(sample: list[int], variations: list[int], func):
    total_time_bi = 0
    total_time_of = 0

    for i in variations:
        start_time = time.time()
        try:
            bild_in_result = sample.index(i)
        except:
            bild_in_result = None
        total_time_bi += time.time() - start_time

        start_time = time.time()
        our_result = func(sample, i)
        total_time_of += time.time() - start_time

        if bild_in_result != our_result:
            print(our_result, bild_in_result)
    print(f'Bild in method: {total_time_bi} Seconds')
    print(f'{func.__name__}: {total_time_of} Seconds')

random_sample = [randrange(-MAX_RANGE, MAX_RANGE) for _ in range(NUM_OF_ELEMENTS)]
#check_with_method(sorted(random_sample), [randrange(-1000, 1000) for _ in range(100)], binary_search)
check(random_sample, sorted, binary_insert_sort)