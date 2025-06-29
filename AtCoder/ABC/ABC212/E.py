import sys
input = sys.stdin.readline
MOD = 998244353

N, M, K = map(int, input().split())
U = [0] * M
V = [0] * M
for i in range(M):
    u, v = map(int, input().split())
    U[i] = u - 1
    V[i] = v - 1

# dp[x] : 指定日後に都市xにいるパスの数
dp = [1] + [0] * (N - 1)

# K日間数え上げる
for _ in range(K):
    # ndp : dpの次の日を計算する用
    # ndp[x] = S - dp[x] - (Edgesに含まれるxからのパスの数) 
    S = sum(dp) % MOD
    ndp = [S - z for z in dp]

    # ローカル束縛で高速化
    uu, vv, dpl = U, V, dp
    for i in range(M):
        a = uu[i]
        b = vv[i]
        pa = dpl[a]
        pb = dpl[b]
        ndp[a] -= pb
        ndp[b] -= pa

    for i in range(N):
        ndp[i] %= MOD
    
    dp = ndp

print(dp[0])