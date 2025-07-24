# 交換した個数を最大化する問題
# KNまでは普通のナップサックで解き、それ以上は最高効率のものを採用する

def main():
    N, M = map(int, input().split())
    T = [0] * 301
    for _ in range(M):
        a, b = map(int, input().split())
        T[a] = max(T[a], b)

    midx = 0
    md = 1000
    for (a, b) in enumerate(T):
        if b == 0:
            continue
        if a > N:
            continue
        d = a - b
        if T[midx] * d < b * md:
            midx = a
            md = d
    
    ans = N
    NN = N
    KN = 10 ** 5
    if NN > KN:
        t = ((NN - KN) // md)
        ans += t * T[midx]
        NN -= t * md

    dp = [0] * (NN + 1)
    for (a, b) in enumerate(T):
        d = a - b
        if a == 0:
            continue
        if a > NN:
            break
        for i in range(b, NN - d + 1):
            dp[i + d] = max(dp[i + d], dp[i] + b)
    
    ans += dp[NN]
    print(ans)

if __name__ == '__main__':
    main()