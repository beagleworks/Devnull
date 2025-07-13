# a, bが決まればcは自動的に決まる
# また a < b であれば a = cより不適、よって N >= a > b
# (a, b) の全組み合わせから a % b == 0となる組み合わせを除外したものが答え

def main():  
    N = int(input())

    k = 0
    i = 1
    MOD = 998244353
    while i <= N:
        p = N // i
        q = N // p
        k += p * (q - i + 1)
        i = q + 1
    print(((N * (N + 1) // 2) - k) % MOD)

if __name__ == '__main__':
    main()
