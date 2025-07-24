def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())

    a = sum(A)
    b = X // a
    rest = X - a * b
    ans = N * b
    cnt = 0
    for i in range(N):
        cnt += A[i]
        if cnt > rest:
            print(ans + i + 1)
            return           

if __name__ == '__main__':
    main()

