MOD = 998244353

A, B, C, D = map(int, input().split())

exA = B + C + D
num = 1
denom = 1

iX = [0] * (B + 1)
iX[1] = 1
for i in range(2, B + 1):
  iX[i] = (MOD - (MOD // i) * iX[MOD % i] % MOD)

suf = [0] * (B + 1)
suf[B] = 1
for k in range(B - 1, -1, -1):
  suf[k] = suf[k + 1] * (exA - k) % MOD

for i in range(C):
  num = num * (exA - i) % MOD

for i in range(1, C + 1):
  denom = denom * i % MOD

f = 1
g = num * pow(denom, MOD-2, MOD) % MOD
pref = 1
h = pow(suf[0], MOD-2, MOD)
ans = 0
for b in range(B + 1):
  ans = (ans + f * g) % MOD
  if b == B:
    break
  df = exA - b
  f = f * (A + b) % MOD * iX[b + 1] % MOD
  iDenom = pref * suf[b + 1] % MOD * h % MOD
  g = g * (df - C) % MOD * iDenom % MOD
  pref = pref * df % MOD

print(ans)