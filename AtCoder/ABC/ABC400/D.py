from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]
A, B, C, D = map(int, input().split())
A -= 1
B -= 1
C -= 1
D -= 1

INF = 10 ** 9
dp = [[INF] * W for _ in range(H)]
dp[A][B] = 0
q = deque([(A, B)])
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while q:
  y, x = q.popleft()
  if y == C and x == D:
    break
  for dy, dx in d:
    ny = y + dy
    nx = x + dx
    nny = ny + dy
    nnx = nx + dx
    if 0 <= ny < H and 0 <= nx < W:
      if S[ny][nx] == '.' and dp[ny][nx] > dp[y][x]:
        dp[ny][nx] = dp[y][x]
        q.appendleft((ny, nx))
      elif S[ny][nx] == '#':
        if dp[ny][nx] > dp[y][x] + 1:
          dp[ny][nx] = dp[y][x] + 1
          q.append((ny, nx))
        if 0 <= nny < H and 0 <= nnx < W:
          if dp[nny][nnx] > dp[y][x] + 1:
            dp[nny][nnx] = dp[y][x] + 1
            q.append((nny, nnx))

print(dp[C][D])