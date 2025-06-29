def main():
    import sys
    input = sys.stdin.readline

    MOD = 998244353

    N = int(input())
    EV = []
    for i in range(N):
        A = list(map(int, input().split()))
        for a in A:
            EV.append((a, i))
    EV.sort()

    iL = [0] * 7
    for k in range(1, 7):
        iL[k] = pow(k, MOD - 2, MOD)

    i6 = iL[6]
    i6_N = pow(i6, N, MOD)

    cnt = N
    seen = [0] * N
    ans = 0
    x, y = 1, 0   

    i = 0
    L = len(EV)
    while i < L:
        v = EV[i][0]
        j = i
        while j < L and EV[j][0] == v:
            dc = EV[j][1]
            pre = seen[dc]
            if pre == 0:
                cnt -= 1

            ftr = pre + 1
            x = (x * ftr) % MOD
            z = pre if pre > 0 else 1
            x = (x * iL[z]) % MOD
            seen[dc] = ftr
            j += 1

        g = x * i6_N % MOD if cnt == 0 else 0
        ans = (ans + (v % MOD) * (g - y)) % MOD
        y = g

        i = j

    print(ans)

if __name__ == "__main__":
    main()