# ダイクストラ法で"1"にするための最短コストを事前計算
def dijkstra(adj, start):
    import heapq

    n = len(adj)
    INF = float('inf')

    # 初期化
    dist = [INF] * n
    prev = [None] * n
    dist[start] = 0

    # (距離, 頂点) のタプルをヒープに入れる
    pq = [(0, start)]

    while pq:
        d_u, u = heapq.heappop(pq)
        # 古いエントリは無視
        if d_u > dist[u]:
            continue

        # 隣接辺をたどる
        for v, w in adj[u]:
            d_v = d_u + w
            if dist[v] > d_v:
                dist[v] = d_v
                prev[v] = u
                heapq.heappush(pq, (d_v, v))

    return dist, prev


def main():
    H, W = map(int, input().split())
    G = [[] for _ in range(10)]
    for i in range(10):
        line = list(map(int, input().split()))
        for j in range(10):
            G[i].append((j, line[j]))

    R = [float('inf')] * 10
    for i in range(10):
        dist, _ = dijkstra(G, i)
        R[i] = dist[1]

    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 0
    for a in A:
        for e in a:
            if e != -1:
                ans += R[e]

    print(ans)


if __name__ == '__main__':
    main()