def getSkyline(arr, n):
    index = 0

    e = []
    pq =[]
    skyline =[]

    for i in range(n):
        e.append((arr[i][0], i))
        e.append((arr[i][1], i))

    e.sort()

    while index<len(e):
        x = e[index][0]

        while index < len(e) and e[index][0] == x:

            building_idx = e[index][1]

            # if building starts
            if arr[building_idx][0] == x:

                # add building to active list
                pq.append((arr[building_idx][2], arr[building_idx][1]))

            index += 1

        pq = [item for item in pq if item[1] > x]

        pq.sort(reverse=True)

        height = 0 if len(pq) == 0 else pq[0][0]

        if len(skyline) == 0 or skyline[-1][1] != height:
            skyline.append((x, height))

    return skyline


print(getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], 5))