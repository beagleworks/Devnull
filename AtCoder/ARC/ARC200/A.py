import sys
# A0Bj != B0Aj となる(u, v) = (0, j) に対して
# X = [Xu, 0,...,0, Xv, 0,...,0] で良い
# Xu = si * (Av + Bv), Xv = -si * (Au + Bu) 
def main():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
    
        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        u = 0
        v = -1
        a0, b0 = A[0], B[0]
        # A[0] / B[0] != A[j] / B[j] となるjを探す
        for j in range(1, N):            
            if a0 * B[j] != b0 * A[j]:
                v = j
                break

        # vが見つからなかった場合は、全ての項が同じ比率 -> No
        if v == -1:
            ans.append("No")
        # 第u項、第v項以外はすべて0        
        else:
            au, av, bu, bv = A[u], A[v], B[u], B[v]

            diff = au * bv - bu * av
            # diffが負なら符号反転
            si = 1 if diff > 0 else -1            
            Xi = si * (av + bv)
            Xj = -si * (au + bu)

            X = ["0"] * N
            X[u] = str(Xi)
            X[v] = str(Xj)

            ans.append("Yes")
            ans.append(" ".join(X))

    print("\n".join(ans))

if __name__ == '__main__':
    main()