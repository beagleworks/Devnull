def main():
    N = int(input())
    A, B = zip(*(map(int, input().split()) for _ in range(N)))
    A, B = list(A), list(B)
    
    t = sum(i / j for i, j in zip(A, B)) / 2
    i = 0
    ans = 0
    while True:
        if t - A[i] / B[i] <= 0:
            print(ans + t * B[i])
            return
        
        t -= A[i] / B[i]
        ans += A[i]
        i += 1
 
if __name__ == '__main__':
    main()
