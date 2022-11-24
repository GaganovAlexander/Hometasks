def bubble_sort(sample: list[int]) -> list[int]:
    sorted_sample = sample.copy()
    run = True
    itteration = 0
    while run:
        run = False
        for i in range(1, len(sorted_sample) - itteration):
            if sorted_sample[i] < sorted_sample[i-1]:
                run = True
                sorted_sample[i-1], sorted_sample[i] = sorted_sample[i], sorted_sample[i-1]
        itteration += 1
    return sorted_sample

def selection_sort(sample: list[int]) -> list[int]:
    sorted_sample = []
    sample = sample.copy()
    for _ in range(len(sample)):
        a = min(sample)
        sorted_sample.append(a)
        sample.remove(a)
    return sorted_sample

def insert_sort(sample: list[int]) -> list[int]:
    sorted_sample = [sample[0]]
    for i in range(1, len(sample)):
        for j in range(len(sorted_sample)):
            if sample[i] < sorted_sample[j]:
                sorted_sample.insert(j, sample[i])
                break
    return sorted_sample        


def simple_search1(sample: list[int], desired: int) -> int:
    for i in range(len(sample)):
        if sample[i] == desired:
            return i
    return None

def simple_search2(sample: list[int], desired: int) -> int:
    index = 0
    for i in sample:
            if i == desired:
                return index
            index += 1
    return None

def binary_search(sorted_sample: list[int], desired: int) -> int:
    left = 0
    right = len(sorted_sample) - 1
    while left < right:
        middle = (left + right) // 2
        if desired > sorted_sample[middle]:
            left = middle + 1
        elif desired < sorted_sample[middle]:
            right = middle - 1
        else:
            while sorted_sample[middle] == desired:
                middle -= 1
            return middle + 1
    if left == right:
        if sorted_sample[left] == desired:
            return left
        else:
            return None
    elif left > right:
        return None
