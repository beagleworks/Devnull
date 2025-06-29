def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    ST = [0] * (N + 2)
    ans = 0
    
    for a in A:
        # 両端の色チェック
        # D : 白白 1 白黒(黒白) 0 黒黒 -1
        D = 1 - ST[a - 1] - ST[a + 1]
        # 白→黒
        if ST[a] == 0:
            ans += D
            ST[a] = 1
        # 黒→白
        else:
            ans -= D
            ST[a] = 0
        print(ans)

if __name__ == '__main__':
    main()