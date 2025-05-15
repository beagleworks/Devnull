from collections import deque

N = int(input())
H = list(map(int, input().split()))

q = deque()
ans = []

for i in range(N - 1, -1, -1):
  ans.append(len(q))
  if len(q) > 0 and q[-1] < H[i]:
    while len(q) > 0 and q[-1] < H[i] :
      q.pop()
  q.append(H[i])

print(*reversed(ans))
