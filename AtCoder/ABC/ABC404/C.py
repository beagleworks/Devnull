import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

A = [[] for _ in range(N)]
D = [0] * N

if M != N:
    print("No")
    exit()

for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    A[a].append(b)
    A[b].append(a)
    D[a] += 1
    D[b] += 1

for x in range(N):
    if D[x] != 2:
        print("No")
        exit()

visited = [False] * N
q = deque([0])
visited[0] = True
cnt = 1
while q:
    p = q.popleft()
    for k in A[p]:
        if not visited[k]:
            visited[k] = True
            cnt += 1
            q.append(k)

print("Yes" if cnt == N else "No")
