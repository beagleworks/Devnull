def main():
    N = int(input())
    A = list(map(int, input().split()))

    st = {}
    ans = 10 ** 7
    for i in range(N):
        if A[i] in st:
            ans = min(ans, i - st[A[i]] + 1)
        st[A[i]] = i

    print(-1 if ans == 10 ** 7 else ans)


if __name__ == '__main__':
    main()
