# トポロジカルソート
# 最初に入力次数が0のものをヒープに入れ、辞書順最小のものから取り出す
# 取り出したものから伸びる有効辺を削除(行先頂点の次数を減らす)、当該頂点をSに追加
# 行き先の頂点の次数0になったらヒープに追加

def main():
    import heapq

    N, M = map(int, input().split())
    R = [[] for _ in range(N)]
    T = [0] * N

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        R[a].append(b)
        T[b] += 1

    S = []
    hq = []
    for i in range(N):
        if T[i] == 0:
            heapq.heappush(hq, i)
    
    while hq:
        v = heapq.heappop(hq)
        S.append(v + 1)
        for u in R[v]:
            T[u] -= 1
            if T[u] == 0:
                heapq.heappush(hq, u)
    
    if len(S) < N:
        print(-1)
    else:
        print(*S)                

 
if __name__ == '__main__':
    main()
