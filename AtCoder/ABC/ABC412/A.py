def main():
    N = int(input())
    ans = 0
    for i in range(N):
        a, b = map(int, input().split())
        if a < b:
            ans += 1
    
    print(ans)

if __name__ == '__main__':
    main()