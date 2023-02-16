def ranking(sample: list[int]) -> list[int]:
    ranks = []
    sorted_list_pos = sorted([x for x in sample if x > 0])
    sorted_list_neg = sorted([x for x in sample if x < 0])
    for i in sample:
        if i > 0:
            rank = sorted_list_pos.index(i) + 1
            ranks.append(rank)
        elif i < 0:
            rank = sorted_list_neg.index(i) + 1
            ranks.append(-rank)
        else:
            ranks.append(0)
    return ranks

def get_splits(sample, x):
    for i in range(0, len(sample)):
        if i + x < len(sample):
            yield i, i + x
        else:
            yield i, len(sample)
        
a = [1, 8, 7, 6, 3, 6]
b = [5, 9, 6, 8, 8, 6]
new_a = []
minim = None
for i in range(2, len(a) + 1):
    for j, k in get_splits(a, i):
        cool_a = a[:j] + list(reversed(a[j:k])) + a[k:]
        if minim is None:
            minim = sum(abs(ranking(cool_a)[i] - ranking(b)[i]) for i in range(len(a)))
            new_a = cool_a
        elif sum(abs(ranking(cool_a)[i] - ranking(b)[i]) for i in range(len(a))) < minim:
            minim = sum([abs(ranking(cool_a)[i] - ranking(b)[i]) for i in range(len(a))])
            new_a = cool_a

print(a, new_a, b, minim, sum([new_a[i] * b[i] for i in range(len(a))]), sep='\n')
