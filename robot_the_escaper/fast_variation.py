def fast_var(map__):
    map_ = map__.copy()
    for i in range(len(map_)):
        for j in range(len(map_[0])):
            if map_[i][j] == 2:
                lab_cords = (i, j)
                break

    temp_points = [lab_cords]

    while temp_points:
        for i in temp_points.copy():
            for j in ((i[0]+1, i[1]), (i[0]-1, i[1]), (i[0], i[1]-1), (i[0], i[1]+1)):
                if len(map_) > j[0] >= 0 and len(map_[0]) > j[1] >= 0 and map_[j[0]][j[1]] == 0:
                    cnt = 0
                    for k in ((j[0]+1, j[1]), (j[0]-1, j[1]), (j[0], j[1]-1), (j[0], j[1]+1)):
                        if len(map_) > k[0] >= 0 and len(map_[0]) > k[1] >= 0 and map_[k[0]][k[1]] == 0:
                            cnt += 1
                    if cnt <= 1:
                        map_[j[0]][j[1]] = 3
                        temp_points.append((j[0], j[1]))
            temp_points.remove(i)
    return map_
    