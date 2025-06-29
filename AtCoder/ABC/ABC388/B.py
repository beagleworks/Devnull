def main():
    N, D = map(int, input().split())
    T, L = zip(*(map(int, input().split()) for _ in range(N)))
    T, L = list(T), list(L)

    X = [0] * N
    for i in range(1, D + 1):
        for j in range(N):
            X[j] = T[j] * (L[j] + i)
        print(max(X))    

if __name__ == '__main__':
    main()
