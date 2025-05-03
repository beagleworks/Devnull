import sys
input = sys.stdin.readline
from collections import defaultdict

N, M, Q = map(int, input().split())

ans = []
allok = [False] * (N + 1)
ok = defaultdict(set)

for _ in range(Q):
  qu = input().split()
  t = int(qu[0])

  if t == 1:
    x, y = map(int, qu[1:])

    if allok[x]:
      continue
    ok[x].add(y)

  elif t == 2:
    x = int(qu[1])  
    allok[x] = True

  else:
    x, y = map(int, qu[1:])
    if allok[x] or y in ok[x]:
      ans.append("Yes")
    else:
      ans.append("No")

print("\n".join(ans))