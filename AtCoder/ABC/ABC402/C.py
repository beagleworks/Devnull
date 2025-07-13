def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    A = []
    X = [[] for _ in range(N + 1)]
    for i in range(M):
        a = list(map(int, input().split()))
        A.append(a[0])
        for e in a[1:]:
            X[e].append(i)

    B = list(map(int, input().split()))
    cnt = 0
    ans = [0]
    for b in B:
        for x in X[b]:
            A[x] -= 1
            if A[x] == 0:
                cnt += 1
        
        ans.append(cnt)
    
    print(*ans[1:])
    
if __name__ == '__main__':
    main()
