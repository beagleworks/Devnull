import sys
input = sys.stdin.readline

N = int(input())
Ad = [[] for _ in range(N + 1)]
U = [0] * N
V = [0] * N
for i in range(1, N):
  u, v = map(int, input().split())
  U[i], V[i] = u, v
  Ad[u].append(v)
  Ad[v].append(u)

t = 0
E = [0] * (N + 1)
X = [0] * (N + 1)
P = [0] * (N + 1)
que = [(1, 0, 0)]
while que:
  cx = que.pop()
  u, p, stat = cx
  if stat == 0:
    P[u] = p
    t += 1
    E[u] = t
    que.append((u, p, 1))
    for w in Ad[u]:
      if w != p:
        que.append((w, u, 0))
  else:
    X[u] = t

for i in range(1, N):
  u, v = U[i], V[i]
  if P[u] == v:
    U[i] = u
  else:
    U[i] = v

bits = [0] * (N + 1)
for i in range(1, N + 1):
  bits[i] = i & -i
total = N

q = int(input())
out = []
for _ in range(q):
  line = input().split()
  if line[0] == '1':
    x = int(line[1])
    w = int(line[2])
    total += w
    idx = E[x]
    while idx <= N:
      bits[idx] += w
      idx += idx & -idx
  else:
    y = int(line[1])
    c = U[y]
    l = E[c]
    r = X[c]
    s, t = 0, 0
    i2 = r
    while i2 > 0:
      s += bits[i2]
      i2 -= i2 & -i2
    i2 = l - 1
    while i2 > 0:
      t += bits[i2]
      i2 -= i2 & -i2
    rr = s - t
    diff = total - 2 * rr
    if diff < 0:
      diff = -diff
    out.append(str(diff))

print('\n'.join(out))