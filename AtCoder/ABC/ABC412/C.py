def solve():
    from bisect import bisect_right
    
    N = int(input())
    S = list(map(int, input().split()))
    SS = sorted(S[1:-1])

    ans = 2
    cur = S[0]
    aim = S[-1]

    while cur * 2 < aim:
        idx = bisect_right(SS, cur * 2)
        if idx == 0 or SS[idx - 1] == cur:
            print(-1)
            return
        if idx == len(SS):
            if cur * 2 < SS[-1]:
                print(-1)
                return
                
        cur = SS[idx - 1]
        ans += 1
    
    print(ans)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()