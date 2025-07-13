def main():
    N, K = map(int, input().split())
    S = input()

    ans = 0
    cnt = 0
    for s in S:
        cnt = (cnt + 1) if s == 'O' else 0
        if cnt == K:
            ans += 1
            cnt = 0

    print(ans)        

if __name__ == '__main__':
    main()
