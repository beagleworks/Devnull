import sys
input = sys.stdin.readline

N, M = map(int, input().split())

SZ = 2 * N + 2
ep = [0] * SZ
bp = [0] * SZ
seg = [None] * M

for i in range(M):
  a, b = map(int, input().split())
  if a > b:
    a, b = b, a
  seg[i] = (a, b)
  ep[a] = 1
  ep[b] = 1
  bp[b] += 1

for i in range(1, SZ):
  ep[i] += ep[i - 1]
  bp[i] += bp[i - 1]

seg.sort(key=lambda x: x[0])

Q = int(input())
qry = [None] * Q
for i in range(Q):
  c, d = map(int, input().split())
  qry[i] = (c, d, i)

qry.sort(key=lambda x: x[0])
BIT = [0] * SZ

def bit_add(arg):
  while arg < SZ:
    BIT[arg] += 1
    arg += arg & -arg

def bit_sum(pos):
  r = 0
  while pos > 0:
    r += BIT[pos]
    pos -= pos & -pos
  return r

ans = [0] * Q
p = 0
for c, d, qi in qry:
  while p < M and seg[p][0] <= c:
    _, bi = seg[p]
    bit_add(bi)
    p += 1
  ans[qi] = ep[d - 1] - ep[c] - 2 * (bp[d - 1] - bit_sum(d - 1))

for e in ans:
  print(e)
