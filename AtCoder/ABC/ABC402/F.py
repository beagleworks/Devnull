from bisect import bisect_right
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 例外
if N == 1:
    print(A[0][0] % M)
    exit()

x = pow(10, N - 1, M)
y = [-1] * (N * N)

for i in range(1, N):
    j = N - i
    if 0 <= j < N:
        y[i * N + j] = i - 1

z = [0]
w = [0]
for _ in range(N):
    z2, w2 = [], []
    for p, q in zip(z, w):
        i, j = divmod(p, N)
        r = (q * 10 + A[i][j]) % M
        if i + 1 < N:
            z2.append(p + N)
            w2.append(r)
        if j + 1 < N:
            z2.append(p + 1)
            w2.append(r)
    z, w = z2, w2

u = [[] for _ in range(N - 1)]
for p, q in zip(z, w):
    g = y[p]
    u[g].append(q)

z = w = None
s, t, v = [], [], []
for g in range(N - 1):
    i = g + 1
    j = N - i
    p = i * N + j

    s.append(p)
    t.append(A[i][j] % M)
    v.append(g)

for _ in range(N - 2):
    s2, t2, v2 = [], [], []
    for p, q, g in zip(s, t, v):
        i, j = divmod(p, N)
        if i + 1 < N:
            nid = p + N
            r = (q * 10 + A[i + 1][j]) % M
            s2.append(nid)
            t2.append(r)
            v2.append(g)
        if j + 1 < N:
            nid = p + 1
            r = (q * 10 + A[i][j + 1]) % M
            s2.append(nid)
            t2.append(r)
            v2.append(g)

    s, t, v = s2, t2, v2

w = [[] for _ in range(N - 1)]
for q, g in zip(t, v):
    w[g].append(q)

ans = 0
for g in range(N - 1):
    a = u[g]
    b = w[g]

    if not a or not b:
        continue

    b.sort()

    m = b[-1]
    for p in a:
        q = (p * x) % M
        lim = M - 1 - q
        idx = bisect_right(b, lim)
        if idx:
            val = q + b[idx - 1]
            if val > ans:
                ans = val

        val2 = q + m
        if val2 >= M:
            val2 -= M
        if val2 > ans:
            ans = val2

print(ans)
