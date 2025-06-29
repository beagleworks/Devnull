# 点1から到達可能点、点Nからの到達可能点(辺を逆向きにする)を網羅し
# ベルマンフォード法で最短経路を求める
# 負サイクルがあれば1を返す
def main():
    import sys
    sys.setrecursionlimit(10 ** 7)

    N, M, P = map(int, input().split())
    A = [[] for _ in range(N)]
    RA = [[] for _ in range(N)]
    E = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        A[a].append((b, c - P))
        RA[b].append(a)
        E.append((a, b, c - P))
    
    reachableN_1 = [False] * N
    def dfs(v):
        reachableN_1[v] = True
        for u in RA[v]:
            if not reachableN_1[u]:
                dfs(u)
    dfs(N - 1)

    reachable0 = [False] * N
    def dfs2(v):
        reachable0[v] = True
        for u, _ in A[v]:
            if not reachable0[u]:
                dfs2(u)
    dfs2(0)

    INF = 10 ** 18
    def bell(s):
        dist = [INF] * N
        dist[s] = 0

        for _ in range(N - 1):
            for v in range(N):
                if not reachable0[v] or not reachableN_1[v]:
                    continue
                for u, c in A[v]:
                    if not reachable0[u] or not reachableN_1[u]:
                        continue
                    if dist[v] != INF and dist[u] > dist[v] + (-c):
                        dist[u] = dist[v] + (-c)
        
        for u, v, w in E:
            if dist[u] != INF and dist[v] > dist[u] + (-w):
                if reachable0[u] and reachableN_1[v]:
                    return 1
        
        return min(0, dist[N - 1])

    ans = bell(0)
    print(-ans)

if __name__ == '__main__':
    main()