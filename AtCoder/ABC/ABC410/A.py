def main():
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())
    ans = 0
    for a in A:
        if K <= a:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()