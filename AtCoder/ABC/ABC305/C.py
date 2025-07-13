def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            cnt = 0
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < H and 0 <= nj < W and S[ni][nj] == '#':
                    cnt += 1
            if cnt >= 2:
                print(i + 1, j + 1)
                return

if __name__ == '__main__':
    main()