import sys
input = sys.stdin.readline
INF = 10**9

N, D, R = map(int, input().split())
H = list(map(int, input().split()))

Ax = [(H[i], i) for i in range(N)]
Ax.sort()

dp = [0] * N
size = 1
while size < N:
    size <<= 1

tree = [-INF] * (2 * size)
p = 0

for k in range(N):
    h, i = Ax[k]
    while p < N and Ax[p][0] <= h - D:
        j = Ax[p][1]
        v = dp[j]
        pos = j + size
        tree[pos] = v
        pos //= 2
        while pos:
            tree[pos] = max(tree[2 * pos], tree[2 * pos + 1])
            pos //= 2
        p += 1

    cur = -INF
    l = max(0, i - R)
    r = i - 1
    if l <= r:
        ll = l + size
        rr = r + size
        while ll <= rr:
            if ll & 1:
                cur = max(cur, tree[ll])
                ll += 1
            if not (rr & 1):
                cur = max(cur, tree[rr])
                rr -= 1
            ll //= 2
            rr //= 2

    l = i + 1
    if l < N:
        r = min(i + R, N - 1)
        if l <= r:
            ll = l + size
            rr = r + size
            while ll <= rr:
                if ll & 1:
                    cur = max(cur, tree[ll])
                    ll += 1
                if not (rr & 1):
                    cur = max(cur, tree[rr])
                    rr -= 1
                ll //= 2
                rr //= 2

    dp[i] = 0 if cur < 0 else cur + 1

print(max(dp))
