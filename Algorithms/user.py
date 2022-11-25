from Tests import *

if __name__ == '__main__':
    list_of_sorts = [bubble_sort, selection_sort, insert_sort, binary_insert_sort, merge_sort, quick_sort, quick_sort_one_for]
    choice = list(map(int, input('Введите номера сортировок через пробел:\n1) bubble sort; 2) selection sort; 3) insert sort; 4) binary insert sort;\
    \n5) merge sort; 6) quick sort; 7) updated quick sort\n').split()))
    choiced_sorts = [list_of_sorts[i-1] for i in choice]
    MAX_RANGE = 10**4    
    NUM_OF_ELEMENTS = 10**4 + 3
    random_sample = [randrange(-MAX_RANGE, MAX_RANGE) for _ in range(NUM_OF_ELEMENTS)]
    check(random_sample, sorted, *choiced_sorts)
