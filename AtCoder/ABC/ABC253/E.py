# 愚直DPはO(NM^2)となりTLE
# 足し合わせるのは(1 ~ j - K) の和 及び (j + K ~ M) の和のため、事前に和を計算しておくことでO(NM)にする
# 後半は累積和により増加値は S(M) - S(j + K - 1)
# ただし、Kが0の場合はM^Nとなる

def main():
    MOD = 998244353

    N, M, K = map(int, input().split())
    if  K == 0:
        print(M ** N % MOD)
        return
    
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for j in range(1, M + 1):
        dp[1][j] = 1

    for i in range(1, N):
        S = [0] * (M + 1)
        for k in range(1, M + 1):
            S[k] = (S[k - 1] + dp[i][k]) % MOD
        
        for j in range(1, M + 1):
            if j - K >= 1:
                dp[i + 1][j] += S[j - K]
            if j + K <= M:
                dp[i + 1][j] += S[M] - S[j + K - 1]
            
            dp[i + 1][j] %= MOD

    print(sum(dp[N]) % MOD)

if __name__ == '__main__':
    main()