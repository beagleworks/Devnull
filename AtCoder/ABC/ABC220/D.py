# dp[i][j] : i番目まで見たときに先頭の数がjである場合の数

def main():
    MOD = 998244353

    N = int(input())
    A = list(map(int, input().split()))
    
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[1][A[0]] = 1
    for i in range(1, N):
        for j in range(10):
            if dp[i][j] == 0:
                continue
            dp[i + 1][(j + A[i]) % 10] += dp[i][j]
            dp[i + 1][(j + A[i]) % 10] %= MOD
            dp[i + 1][(j * A[i]) % 10] += dp[i][j]
            dp[i + 1][(j * A[i]) % 10] %= MOD

    print(*dp[N])

if __name__ == '__main__':
    main()
