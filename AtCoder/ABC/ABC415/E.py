# 最終日から逆算して、初日にいくらあれば倒れないかをdpで求める

def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    P = list(map(int, input().split()))

    dp = [[10 ** 18] * W for _ in range(H)]
    dp[H - 1][W - 1] = 0

    for i in range(H - 1, -1, -1):
        for j in range(W - 1, -1, -1):
            if i + 1 < H:
                dp[i][j] = min(dp[i][j], dp[i + 1][j])
            if j + 1 < W:
                dp[i][j] = min(dp[i][j], dp[i][j + 1])
            dp[i][j] = max(dp[i][j] - A[i][j] + P[i + j], 0)
    
    print(dp[0][0])

if __name__ == '__main__':
    main()