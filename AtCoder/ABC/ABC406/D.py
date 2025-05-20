import sys
input = sys.stdin.readline

H, W, N = map(int, input().split())
row = [[] for _ in range(H)]
col = [[] for _ in range(W)]
for _ in range(N):
  x, y = map(int, input().split())
  x -= 1; y -= 1
  row[x].append(y)
  col[y].append(x)

row_del = [False] * H
col_del = [False] * W
Q = int(input())
ans = []
for _ in range(Q):
  t, v = map(int, input().split())
  if t == 1:
    x = v - 1
    if row_del[x]:
      ans.append('0')
    else:
      cnt = 0
      for y in row[x]:
        if not col_del[y]:
          cnt += 1
      row_del[x] = True
      ans.append(str(cnt))
  else:
    y = v - 1
    if col_del[y]:
      ans.append('0')
    else:
      cnt = 0
      for x in col[y]:
        if not row_del[x]:
          cnt += 1
      col_del[y] = True
      ans.append(str(cnt))

print('\n'.join(ans))