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
    import math
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

    # 結果をリストにまとめて返却
    return [A + i for i, flag in enumerate(is_prime) if flag]


# Example usage
PP = Eratosthenes(457)
QQ = Eratosthenes2(25, 100)
print(PP)
print(QQ)


