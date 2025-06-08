from collections import deque
import bisect
import sys
sys.setrecursionlimit(10 ** 6)

N1 = int(input())
V1 = [[] for _ in range(N1)]
for i in range(N1 - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    V1[u].append(v)
    V1[v].append(u)

N2 = int(input())
V2 = [[] for _ in range(N2)]
for i in range(N2 - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    V2[u].append(v)
    V2[v].append(u)


def bfs(p, adj):
    n = len(adj)
    dist = [-1] * n
    dq = deque([p])
    dist[p] = 0
    while dq:
        u = dq.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq.append(v)
    return dist

# 直径 D と、各頂点 i の「直径の端点 a, b からの距離の大きい方」を返す


def precalc_tree(adj):
    pd = bfs(0, adj)
    a = max(range(len(adj)), key=lambda i: pd[i])
    dist_a = bfs(a, adj)
    b = max(range(len(adj)), key=lambda i: dist_a[i])
    D = dist_a[b]
    dist_b = bfs(b, adj)
    x = [dist_a[i] if dist_a[i] > dist_b[i] else dist_b[i]
         for i in range(len(adj))]
    return D, x


D1, A = precalc_tree(V1)
D2, B = precalc_tree(V2)
DD = max(D1, D2)

B.sort()
Bsum = [0] * (N2 + 1)
for i in range(N2):
    Bsum[i + 1] = Bsum[i] + B[i]

ans = 0
for a in A:
    idx = bisect.bisect_left(B, DD - a - 1)
    ans += idx * DD + (N2 - idx) * (a + 1) + Bsum[N2] - Bsum[idx]

print(ans)
