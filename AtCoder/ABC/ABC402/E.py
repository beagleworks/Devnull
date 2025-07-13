# 期待値のbitDP
# dp[bit][spent] = P * (該当の問題のスコア + dp[bit|i][spent + cost]: 提出が成功した場合の遷移先) + (1 - P) * (dp[bit][spent + cost]: 提出が失敗した場合の遷移先)
def main():
    N, X = map(int, input().split())
    Q = [tuple(int(x) for x in input().split()) for _ in range(N)] # Score,Cost,Probability
    
    dp = [[0.0] * (X + 1) for _ in range(1 << N)]

    for spent in range(X, -1, -1):
        for bit in range(1 << N):
            for i in range(N):
                if bit & (1 << i):
                    continue
                if spent + Q[i][1] <= X: 
                    dp[bit][spent] = max(dp[bit][spent], (dp[bit | (1 << i)][spent + Q[i][1]] + Q[i][0]) * (Q[i][2] / 100.0) + (dp[bit][spent + Q[i][1]]) * (1 - (Q[i][2] / 100.0)))


    print(dp[0][0])

if __name__ == '__main__':
    main()
