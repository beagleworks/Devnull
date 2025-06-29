def main():
    H, W, N = list(map(int, input().split()))
    R, C = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        R.append(a)
        C.append(b)

    # 座標圧縮
    def shrink(X):
        return {x: i for i, x in enumerate(sorted(set(X)))}

    RS = shrink(R)
    CS = shrink(C)
    for i in range(N):
        print(RS[R[i]] + 1, CS[C[i]] + 1)

if __name__ == '__main__':
    main()