import heapq

Q = int(input())

hq = []
k = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heapq.heappush(hq, q[1] - k)
    elif q[0] == 2:
        k += q[1]
    else:
        print(heapq.heappop(hq) + k)

