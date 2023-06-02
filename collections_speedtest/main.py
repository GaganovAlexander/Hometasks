from numpy import array as np_array
from numpy import int32, ndarray, append

from array import array
from collections import deque
from time import perf_counter


LIST_ = list(map(lambda x: x**2, range(10**4)))

def change_test(collection):
    start = perf_counter()
    for i in collection:
        i += 1
    print(perf_counter() - start, type(collection))

def append_test(collection):
    if isinstance(collection, ndarray):
        start = perf_counter()
        for i in range(10**3):
            append(collection, i)
        print(perf_counter() - start, type(collection))
        return
    start = perf_counter()
    for i in range(10**3):
        collection.append(i)
    print(perf_counter() - start, type(collection))


if __name__ == '__main__':
    np_array_ = np_array(LIST_, int32)
    array_ = array('i', LIST_)
    deque_ = deque(LIST_, 10**4+10**3)
    print('Change data speed test')
    change_test(LIST_)
    change_test(np_array_)
    change_test(array_)
    change_test(deque_)

    print('Append data speed test')
    append_test(LIST_)
    append_test(np_array_)
    append_test(array_)
    append_test(deque_)