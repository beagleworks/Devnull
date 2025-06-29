def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        cnt = 0
        A = list(map(int, input().split()))
        for idx, a in enumerate(A):
            cnt += a * B[idx] 
        if cnt + C > 0:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()