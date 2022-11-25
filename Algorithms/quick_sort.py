def quick_sort(sample: list[int]) -> list[int]:
    if len(sample) <= 1:
        return sample
    else:
        leasser = [i for i in sample if i < sample[0]]
        equal = [i for i in sample if i == sample[0]]
        greater = [i for i in sample if i > sample[0]]
        return quick_sort(leasser) + equal + quick_sort(greater)

def quick_sort_one_for(sample: list[int]) -> list[int]:
    if len(sample) <= 2:
        if len(sample) == 2:
            if sample[0] > sample[1]:
                return sample[::-1]
            else:
                return sample
        else:
            return sample
    else:
        leasser = []
        equal = []
        greater = []
        for i in sample:
            if i < sample[0]:
                leasser.append(i)
            elif i > sample[0]:
                greater.append(i)
            else:
                equal.append(i)
        return quick_sort(leasser) + equal + quick_sort(greater)
