def main():
    N, M = map(int, input().split())
    A = sorted([tuple(map(int, input().split())) for _ in range(N)])

    cnt = 0
    ans = 0
    idx = 0
    while cnt < M:
        a, b = A[idx]
        if cnt + b > M:
            ans += a * (M - cnt)
            break

        ans += a * b
        cnt += b
        idx += 1
    
    print(ans)

if __name__ == '__main__':
    main()