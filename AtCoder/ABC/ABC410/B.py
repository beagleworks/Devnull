def main():
    N, Q = map(int, input().split())
    X = list(map(int, input().split()))

    ans = [0] * (N + 1)
    for x in X:
        if x == 0:
            tmp = 10 ** 6
            idx = 0
            for i in range(1, N + 1):
                 if ans[i] < tmp:
                    tmp = ans[i]
                    idx = i
            ans[idx] += 1
            print(idx)
        else:
            ans[x] += 1
            print(x)

if __name__ == '__main__':
    main()