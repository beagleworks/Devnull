# {1, 2, ..., K}, {2, 3, ..., K + 1}, ..., {N - K + 1, N - K + 2, ..., N}
# の、各集合に対して最大index - 最小indexを求め、最小値がans

def main():
    from sortedcontainers import SortedSet

    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = [0] * (N + 1)
    for i in range(N):
        Q[P[i]] = i 
    S = SortedSet()

    for i in range(1, K + 1):
        S.add(Q[i])
    
    ans = S[-1] - S[0]
    for i in range(K + 1, N + 1):
        S.add(Q[i])
        S.remove(Q[i - K])
        ans = min(ans, S[-1] - S[0])

    print(ans)

if __name__ == '__main__':
    main()
