# 正しい括弧列の条件として、区間L, Rの部分和が0かつ、min(PS[L:R]) >= 0であること
# 累積和をLazySegTreeに乗せる
# op: min(x, y) e: INF mapping: x + f composition: f + g id_: 0 

def main():
    from atcoder.lazysegtree import LazySegTree

    N, Q = map(int, input().split())
    S = input()
    P = [1 if S[i] == '(' else -1 for i in range(N)]
    PS = [0] * (N + 1)
    for i in range(N):
        PS[i + 1] = PS[i] + P[i]

    def op(x, y):
        return min(x, y)
    
    e = float("inf")

    def mapping(f, x):
        return x + f
    
    def composition(f, g):
        return f + g
    
    id_ = 0
    
    LST = LazySegTree(op, e, mapping, composition, id_, PS[1:])

    for _ in range(Q):
        q, l, r = map(int, input().split())
        l -= 1
        r -= 1
        if q == 1:
            if P[l] != P[r]:
                d = 2 if P[l] < P[r] else -2
                LST.apply(l, r, d)
                P[l], P[r] = P[r], P[l]
        
        else:
            if l == 0:
                st = 0
            else:
                st = LST.get(l - 1)
            
            t = LST.get(r) - st
            mn = LST.prod(l, r + 1) - st
            print("Yes" if t == 0 and mn >= 0 else "No")

 
if __name__ == '__main__':
    main()