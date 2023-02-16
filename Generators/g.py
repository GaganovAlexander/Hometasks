from math import sqrt


l1 = [sqrt(x) for x in range(1001) if x % 3]

l2 = [[sqrt(x) for x in range(i-9, i-1) if x % 3] for i in range(10, 1001, 9)]
for i in l2:
    print(i, len(i))


a = [sqrt(x) for x in range(1001)]
a1 =list(map(sqrt, range(1001)))