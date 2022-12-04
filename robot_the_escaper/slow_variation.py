def slow_var(map__):
    map_ = map__.copy()
    run = True
    while run:
        run = False
        for i in range(len(map_)):
            for j in range(len(map_[0])):
                cnt = 0
                path = False
                for k in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= k[0] < len(map_) and 0 <= k[1] < len(map_[0]):
                        if map_[k[0]][k[1]] == 0:
                            cnt += 1
                        if map_[k[0]][k[1]] in (2, 3):
                            path = True
                if cnt <= 1:
                    if map_[i][j] not in [1, 2, 3] and path:
                        map_[i][j] = 3
                        run = True
    return map_
    