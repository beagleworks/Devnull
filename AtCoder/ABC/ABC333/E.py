N = int(input())

fm = [0] * N
T = []
X = []

for i in range(N):
  t, x = map(int, input().split())
  T.append(t)
  X.append(x - 1)

K = 0
tK = 0
ans = []
for i in range(N - 1, -1, -1):
  t, x = T[i], X[i]
  if t == 1:
    if fm[x] == 0:
      ans.append('0')
    else:
      fm[x] -= 1
      ans.append('1')
      tK -= 1
  else:
    fm[x] += 1
    tK += 1
    K = max(tK, K)

if any(e != 0 for e in fm):
  print(-1)
  exit()

print(K)
print(" ".join(reversed(ans)))
