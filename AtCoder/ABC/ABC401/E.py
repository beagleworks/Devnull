import sys
input = sys.stdin.readline

N, M = map(int, input().split())
min_nbr = [N + 1] * (N + 1)
edges_by_max = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    min_nbr[v] = min(min_nbr[v], u)
    edges_by_max[v].append((u, v))

diff = [0] * (N + 3)
for j in range(2, N + 1):
    mn = min_nbr[j]
    if mn <= N:
        l = mn
        r = j - 1
        if l <= r:
            diff[l] += 1
            diff[r + 1] -= 1

bnc = [0] * (N + 2)
cur = 0
for k in range(1, N + 1):
    cur += diff[k]
    bnc[k] = cur

parent = list(range(N + 1))
sz = [1] * (N + 1)


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if sz[a] < sz[b]:
        a, b = b, a
    parent[b] = a
    sz[a] += sz[b]


ans = []
for k in range(1, N + 1):
    for u, v in edges_by_max[k]:
        union(u, v)
    if sz[find(1)] == k:
        ans.append(str(bnc[k]))
    else:
        ans.append(str(-1))

print('\n'.join(ans))
