def main():
    N = int(input())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    sa = sum(A)
    ans = max(sa + (B[i] - A[i]) for i in range(N))
    print(ans)

if __name__ == '__main__':
    main()
