import sys

def main():
    input = sys.stdin.readline

    N, H, M = map(int, input().split())
    Dec = [tuple(map(int, input().split())) for _ in range(N)]

    # dp[x] : 体力がx減ったときに保有できる魔力の最大値
    dp = [-1] * (H + 1)
    dp[0] = M

    ans = 0
    for a, b in Dec:
        dp2 = [-1] * (H + 1)
        f = False

        for h in range(H + 1):
            v = dp[h]
            if v < 0:
                continue

            p1 = h + a
            if p1 <= H and dp2[p1] < v:
                dp2[p1] = v
                f = True

            if v >= b:
                p2 = v - b
                if dp2[h] < p2:
                    dp2[h] = p2
                    f = True
        if not f:
            break

        dp = dp2
        ans += 1

    print(ans)

if __name__ == "__main__":
    main()