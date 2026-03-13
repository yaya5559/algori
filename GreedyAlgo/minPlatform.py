import heapq



def minPlatforn(arr, dep):
    trains = list(zip(arr, dep))

    trains.sort()

    pq = []
    res = 0

    for train in trains:

        while pq and pq[0][1]<train[0]:
            heapq.heappop(pq)

        heapq.heappush(pq, train)
        res = max(res, len(pq))
        

    return res


arr = [900, 1000]
dep = [1000, 1100]

print(minPlatforn(arr, dep))
