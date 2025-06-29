# 次数が2である連結成分の頂点数は3以上、N <= 8 より連結成分は2つ以下
# 連結成分が1つのときと2つのときを全列挙して調べる
def main():
    from itertools import permutations
    N, M = map(int, input().split())
    E = [[False] * N for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        E[a][b] = E[b][a] = True
    
    V = list(range(N))
    V = permutations(V, N)
    ans = 10 ** 5

    for perm in V:
        # 連結成分が1つ→この頂点順にサイクル
        F = [[False] * N for _ in range(N)]
        for i in range(N):
            F[perm[i]][perm[(i + 1) % N]] = F[perm[(i + 1) % N]][perm[i]] = True
        ans = min(ans, sum(E[i][j] != F[i][j] for i in range(N) for j in range(N)) // 2)
    
        # 連結成分が2つ→実際にこの並び順で2つのサイクルを作成
        for i in range(3, N - 2):
            G = [[False] * N for _ in range(N)]
            for j in range(i):
                G[perm[j]][perm[(j + 1) % i]] = G[perm[(j + 1) % i]][perm[j]] = True
            for j in range(i, N):
                G[perm[j]][perm[i + (j + 1 - i) % (N - i)]] = G[perm[i + (j + 1 - i) % (N - i)]][perm[j]] = True
            ans = min(ans, sum(E[i][j] != G[i][j] for i in range(N) for j in range(N)) // 2)
    
    print(ans)

if __name__ == '__main__':
    main()
