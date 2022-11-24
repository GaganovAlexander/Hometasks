def quick_sort(sample: list[int]) -> list[int]:
    if len(sample) <= 1:
        return sample
    else:
        leasser = [i for i in sample if i < sample[0]]
        equal = [i for i in sample if i == sample[0]]
        greater = [i for i in sample if i > sample[0]]

        return quick_sort(leasser) + equal + quick_sort(greater)