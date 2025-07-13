def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = sorted([(a, i) for i, a in enumerate(A)], reverse=True)

    if N == 1:
        print(1)
        return

    ans = -1
    tmp = -1
    f = False
    for i in range(N):
        if B[i][0] == tmp:
            f = False
            continue
        if f and tmp != B[i][0]:
            print(ans)
            return
        else:
            tmp = B[i][0]
            ans = B[i][1] + 1
            f = True
            if i == N - 1:
                print(ans)
                return

    print(-1)
        
if __name__ == '__main__':
    main()
