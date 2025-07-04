# エラトステネスの篩で立方根N以下の素数を全列挙
# 各pについて、二分探索でqの個数を求めて足し合わせる
def main():
    import math
    from bisect import bisect_left   

    N = int(input())
    
    def Eratosthenes(N):

        isprime = [True] * (N + 1)
        isprime[0], isprime[1] = False, False

        for p in range(2, N + 1):
            if not isprime[p]:
                continue

            q = p * 2
            while q <= N:
                isprime[q] = False
                q += p

        ret = []
        for i in range(N + 1):
            if isprime[i]:
                ret.append(i)
        
        return ret
    
    pm = math.floor(pow(N, 1/3))
    S = Eratosthenes(pm)
    
    ans = 0
    for i in range(len(S)):
        left = i
        right = len(S)
        while right - left > 1:
            mid = left + (right - left) // 2
            if S[i] * (S[mid] ** 3) <= N:
                left = mid
            else:
                right = mid
        ans += left - i

    print(ans)

if __name__ == '__main__':
    main()