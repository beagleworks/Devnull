# 最小公倍数の数が増えるときは、ある素数の指数が初めて増えるとき
# ある素数の指数が増える最小の値は、その素数の冪乗であるとき(素数冪)
# つまり L ~ R 間の素数(の1乗) + 1 ~ R までの素数の冪乗(>=2乗)の個数が答え

import math

# 1 以上 N 以下の整数の素数を返す
def Eratosthenes(N):

    isprime = [True] * (N + 1)
    isprime[0] = isprime[1] = False

    i = 2
    while i * i <= N:
        if isprime[i]:
            for j in range(i * i, N + 1, i):
                isprime[j] = False
        i += 1

    return [i for i, v in enumerate(isprime) if v]

# 区間 [A, B] の素数を返す(区間篩)
def Eratosthenes2(A, B):

    # √B までの素数を取得
    limit = int(math.isqrt(B))
    small_primes = Eratosthenes(limit)

    is_prime = [True] * (B - A + 1)

    # small_primes を使って区間内の合成数をはじく
    for p in small_primes:
        # p の倍数で最小の >= A の値
        start = max(p * p, ((A + p - 1) // p) * p)
        for multiple in range(start, B + 1, p):
            is_prime[multiple - A] = False

    # A が 1 の場合は素数ではないのではじく
    if A == 1:
        is_prime[0] = False

    # √Bまでの素数と、A~B間の素数をリストにまとめて返却
    return small_primes, [A + i for i, flag in enumerate(is_prime) if flag]

def main():
    L, R = map(int, input().split())

    E1, E2 = Eratosthenes2(L, R)
    ans = 1 + len(E2) - E1.count(L) - E2.count(L)

    for e in E1:
        t = e * e
        while t <= R:
            if L < t:
                ans += 1
            t *= e     
    
    print(ans)


if __name__ == '__main__':
    main()
