import sys
sys.setrecursionlimit(10 ** 8)

N, M = map(int, input().split())
C = list(map(int, input().split()))

zs = [[] for _ in range(N)]
for i in range(M):
    line = list(map(int, input().split()))
    for x in line[1:]:
        zs[x - 1].append(i)

ans = 10 ** 24
cs = [0] * M


def dfs(j, cost):
    global ans
    if j == N:
        if all(c >= 2 for c in cs):
            ans = cost
        return

    if cost < ans:
        dfs(j + 1, cost)

    p = cost + C[j]
    if p < ans:
        for s in zs[j]:
            cs[s] += 1
        dfs(j + 1, p)

        q = p + C[j]
        if q < ans:
            for s in zs[j]:
                cs[s] += 1
            dfs(j + 1, q)

            for s in zs[j]:
                cs[s] -= 1

        for s in zs[j]:
            cs[s] -= 1


dfs(0, 0)
print(ans)
