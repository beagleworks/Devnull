def main():
    H, W, N = map(int, input().split())
    T = input()
    S = [input() for _ in range(H)]
    ans = 0

    d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for i in range(H):
        for j in range(W):
            if S[i][j] != '.':
                continue
            f = True
            ii, jj = i, j
            for c in T:
                di, dj = d[c]
                ni, nj = ii + di, jj + dj
                if ni < 0 or nj < 0 or ni >= H or nj >= W or S[ni][nj] != '.':
                    f = False
                    break
                ii, jj = ni, nj
            if f:
                ans += 1

    print(ans)

if __name__ == '__main__':
    main()
