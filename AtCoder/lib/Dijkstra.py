def dijkstra(adj, start):
    """
    ダイクストラ法

    Parameters
    ----------
    adj : list of list of (int, float)
        隣接リスト。adj[u] = [(v, w), …]
    start : int
        始点の頂点番号

    Returns
    -------
    dist : list of float
        各頂点への最短距離（到達不可能なら float('inf')）
    prev : list of int or None
        最短経路再構築用
    """
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


# --- 使い方の例 ---
if __name__ == '__main__':
    # 4頂点の例グラフ
    # 0 → 1 （重み2）, 0 → 2（重み5）
    # 1 → 2 （重み1）
    # 2 → 3 （重み2）
    # 頂点3からは辺なし
    adj_example = [
        [(1, 2), (2, 5)],
        [(2, 1)],
        [(3, 2)],
        []
    ]

    # 頂点0を始点として実行
    dist, prev = dijkstra(adj_example, start=0)
    print("最短距離:", dist)    # → [0, 2, 3, 5]
    print("経路:", prev)    # → [None, 0, 1, 2]
