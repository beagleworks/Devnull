from math import isqrt

N = int(input())

ans = 0
for a in range(1, 61):
  t = isqrt(N // (2 ** a))
  ans += (t + 1) // 2

print(ans)