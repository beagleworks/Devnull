def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 6)    

    N, Q = map(int, input().split())
    
    V = [(-1, "")]
    P = [0] * (N + 1)

    ID = 1
    for _ in range(Q):
        query = input().split()
        t, p = int(query[0]), int(query[1])

        if t == 1:
            P[p] = P[0]
        elif t == 2:
            s = query[2]
            V.append((P[p], s))
            P[p] = ID
            ID += 1
        else:
            P[0] = P[p]

    tmp = []
    cur = P[0]
    while cur != -1:
        pd, s = V[cur]
        if s:
            tmp.append(s)
        cur = pd
    ans = "".join(reversed(tmp))
    print(ans)

if __name__ == "__main__":
    main()