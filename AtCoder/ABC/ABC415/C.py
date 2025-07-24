def solve():
    N = int(input())
    S = "0" + input()

    dp = [False] * (1 << N)
    dp[0] = True
    for i in range(1 << N):
        if not dp[i]:
            continue
        for bit in range(N):
            if i & (1 << bit):
                continue
            if S[i | (1 << bit)] == "0":
                dp[i | (1 << bit)] = True
    
    print("Yes" if dp[(1 << N) - 1] else "No")
            
def main0():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main0()