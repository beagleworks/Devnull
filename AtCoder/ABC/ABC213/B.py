def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = max(A)
    tmp = 0
    ans = -1
    for i, a in enumerate(A):
        if a == m:
            continue
        if a > tmp:
            tmp = a
            ans = i + 1

    print(ans)

if __name__ == '__main__':
    main()