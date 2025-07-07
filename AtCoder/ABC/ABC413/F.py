# ゴールからの多始点BFS
# 各点について、1回目に訪問するムーブは青木くんに妨害されるため、2回目の訪問がゴールまでの最短となる

def main():
    from collections import deque
    INF = float('inf')

    H, W, K = map(int, input().split())
    dist = [[INF] * W for _ in range(H)]
    cnt = [[0] * W for _ in range(H)]

    q = deque()
    for _ in range(K):
        y, x = map(int, input().split())
        y -= 1
        x -= 1
        q.append((y, x))
        dist[y][x] = 0
        cnt[y][x] = 2

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    while q:
        y, x = q.popleft()
        for i in range(4):
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < H and 0 <= X < W:
                cnt[Y][X] += 1
                if cnt[Y][X] == 2:
                    dist[Y][X] = dist[y][x] + 1
                    q.append((Y, X))
    
    print(sum(sum(e for e in row if e != INF) for row in dist))

if __name__ == '__main__':
    main()