# 半分全列挙
# どのルートも左下から右上の対角線上を必ず1回通るため、この対角線上の点までのルート + 対角線上から(N, N)までのルート の 和のMODが最大のものを探す
# 対角線上から(N, N)までのルート は 逆に考え (N, N)から対角線上までのルートを考える
def main():
    from bisect import bisect_left

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    H1 = [[] for _ in range(N)]
    for bit in range(1 << (N - 1)):
        x, y = 0, 0
        cnt = 0
        for i in range(N - 1):
            cnt *= 10
            cnt %= M
            cnt += A[x][y]
            cnt %= M

            if bit & (1 << i):
                x += 1
            else:
                y += 1
        
        cnt *= 10
        cnt %= M
        cnt += A[x][y]
        cnt %= M

        cnt *= pow(10, N - 1, M)
        H1[x].append(cnt % M)
    
    H2 = [[] for _ in range(N)]
    for bit in range(1 << (N - 1)):
        x, y = N - 1, N - 1
        cnt = 0
        for i in range(N - 1):
            cnt += A[x][y] * pow(10, i, M)
            cnt %= M

            if bit & (1 << i):
                x -= 1
            else:
                y -= 1
        
        H2[x].append(cnt)
    
    ans = 0
    for i in range(N):
        H2[i].sort()
        for h1 in H1[i]:
            idx = bisect_left(H2[i], M - h1)
            ans = max(ans, ((h1 + (H2[i][idx - 1])) % M if idx >= 0 else 0))
    
    print(ans)

if __name__ == '__main__':
    main()
