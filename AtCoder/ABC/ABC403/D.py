import sys
input = sys.stdin.readline
from collections import defaultdict

N, D = map(int, input().split())
A = list(map(int, input().split()))

# エッジケース
if D == 0:
  print(N - len(set(A)))
  exit()

# freq: 出現頻度
freq = defaultdict(int)
for e in A:
  freq[e] += 1

G = defaultdict(list)
for e, cnt in freq.items():
  r = e % D
  k = (e - r) // D
  G[r].append((k, cnt))

total = 0

for items in G.values():
  items.sort()
  sp = 0
  tp = 0
  prev_k = None
  for k, cnt in items:
    if prev_k is not None and k != prev_k + 1:
      total += max(sp, tp)
      sp = 0
      tp = 0

    cs = max(sp, tp)
    ct = sp + cnt
    sp, tp = cs, ct
    prev_k = k

  total += max(sp, tp)

print(N - total)

