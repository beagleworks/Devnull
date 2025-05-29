import heapq

T = int(input())
for _ in range(T):
  N = int(input())
  heap = []
  ans = 0
  for i in range(2 * N):
    a = int(input())
    heapq.heappush(heap, -a)
    z = (i + 1) // 2
    if len(heap) > z:
      ans += -heapq.heappop(heap)
  print(ans)