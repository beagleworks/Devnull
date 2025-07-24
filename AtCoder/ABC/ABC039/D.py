def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    ans = [['.'] * W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                continue
            f = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= H or nj >= W:
                    continue
                if S[ni][nj] == '.':
                    f = False
            if f:
                ans[i][j] = '#'
    
    tmp = [['.'] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if ans[i][j] == '.':
                continue
            tmp[i][j] = '#'
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= H or nj >= W:
                    continue
                tmp[ni][nj] = '#'


    if tmp == S:
        print("possible")
        for row in ans:
            print(''.join(row))
    else:
        print("impossible")

if __name__ == '__main__':
    main()