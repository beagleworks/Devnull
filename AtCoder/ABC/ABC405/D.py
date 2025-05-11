import sys
from collections import deque
input = sys.stdin.readline
INF = 10 ** 10

H, W = map(int, input().split())
field = [list(input().rstrip()) for _ in range(H)]

dist = [[INF] * W for _ in range(H)]
q = deque()
for i in range(H):
  for j in range(W):
    if field[i][j] == 'E':
      dist[i][j] = 0
      q.append((i, j))

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
  x, y = q.popleft()
  for dx, dy in D:
    nx, ny = x + dx, y + dy
    if 0 <= nx < H and 0 <= ny < W and field[nx][ny] != '#' and dist[nx][ny] == INF:
      dist[nx][ny] = dist[x][y] + 1
      q.append((nx, ny))

for i in range(H):
  for j in range(W):
    if field[i][j] == '.':
      d = dist[i][j]
      for dx, dy, dir in [(-1, 0, '^'), (1, 0, 'v'), (0, -1, '<'), (0, 1, '>')]:
        ni, nj = i + dx, j + dy
        if 0 <= ni < H and 0 <= nj < W and dist[ni][nj] == d - 1:
          field[i][j] = dir
          break

for o in field:
  print(''.join(o))