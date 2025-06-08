N = int(input())

if N == 1:
    print(1)
    print(1)

else:
    k = N // 2
    ans = [2 * i for i in range(1, k + 1)]
    print(k)
    print(*ans)
