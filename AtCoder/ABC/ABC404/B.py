N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]
ans = N * N + 10

def rotate(r, i, j):
  if r == 0:
    return S[i][j]
  if r == 1:
    return S[N-1-j][i]
  if r == 2:
    return S[N-1-i][N-1-j]
  return S[j][N-1-i]

for r in range(4):
  cnt = 0
  for i in range(N):
    for j in range(N):
      if rotate(r, i, j) != T[i][j]:
        cnt += 1

  ans = min(ans, r + cnt)

print(ans)