def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict

    N = int(input())
    dct = defaultdict(int)
    for _ in range(N):
        S = str(sorted(input().rstrip()))
        dct[S] += 1
    
    ans = 0
    for v in dct.values():
        ans += (v * (v - 1)) // 2
    print(ans)

if __name__ == '__main__':
    main()