import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    A[u].append((v, w))
    A[v].append((u, w))

ans = 0
fbits = 0

visited = [0] * N
vd = 1
for b in range(29, -1, -1):
    stat = fbits | (1 << b)
    vd += 1
    q = deque([0])
    visited[0] = vd
    found = False

    while q:
        u = q.popleft()
        if u == N - 1:
            found = True
            break
        for tt, w in A[u]:
            if visited[tt] != vd and (w & stat) == 0:
                visited[tt] = vd
                q.append(tt)

    if found:
        fbits = stat
    else:
        ans |= (1 << b)

print(ans)
