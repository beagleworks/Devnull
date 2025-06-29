def main():
    N = int(input())
    D = list(map(int, input().split()))

    for i in range(N - 1):
        ans = []
        d = 0
        for j in range(i, N - 1):
            d += D[j]
            ans.append(d)
        print(*ans)
    
if __name__ == '__main__':
    main()
