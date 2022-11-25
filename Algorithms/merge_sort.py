def merge(list1, list2):
    index1 = 0
    index2 = 0
    new_list = []
    while len(new_list) < len(list1) + len(list2) and index1 < len(list1) and index2 < len(list2):
        if list1[index1] < list2[index2]:
            new_list.append(list1[index1])
            index1 += 1
        else:
            new_list.append(list2[index2])
            index2 += 1
    if index1 < len(list1):
        new_list.extend(list1[index1:])
    if index2 < len(list2):
        new_list.extend(list2[index2:])
    return new_list

def merge_sort(sample: list[int]) -> list[int]:
    devided_sample = [sample]
    while max(map(len, devided_sample)) > 2:
        devided_d_sample = []
        for i in range(len(devided_sample)):
            devided_d_sample.append(devided_sample[i][:len(devided_sample[i])//2]) 
            devided_d_sample.append(devided_sample[i][len(devided_sample[i])//2:]) 
        devided_sample = devided_d_sample.copy()

    for i in range(len(devided_sample)):
        if len(devided_sample[i]) == 2:
            if devided_sample[i][0] > devided_sample[i][1]:
                devided_sample[i] = devided_sample[i][::-1]
                
    while len(devided_sample) > 1:
        new_devided_sample = []
        for i in range(0, len(devided_sample) - 1, 2):
            new_devided_sample.append(merge(devided_sample[i], devided_sample[i + 1]))
        if len(devided_sample) % 2 and len(devided_sample) != 1:
            new_devided_sample.append(devided_sample[-1])
        devided_sample = new_devided_sample.copy()
    return devided_sample[0]

def merge_sort_without_rec(sample: list[int]) -> list[int]:
    devided_sample = []
    for i in range(0, len(sample) - 1, 2):
        if sample[i] <= sample[i + 1]:
            devided_sample.append([sample[i], sample[i + 1]])
        else:
            devided_sample.append([sample[i + 1], sample[i]])
    if len(sample) % 2:
        devided_sample.append([sample[-1]])

    while len(devided_sample) > 1:
        new_devided_sample = []
        for i in range(0, len(devided_sample) - 1, 2):
            new_devided_sample.append(merge(devided_sample[i], devided_sample[i + 1]))
        if len(devided_sample) % 2 and len(devided_sample) != 1:
            new_devided_sample.append(devided_sample[-1])
        devided_sample = new_devided_sample.copy()
    return devided_sample[0]