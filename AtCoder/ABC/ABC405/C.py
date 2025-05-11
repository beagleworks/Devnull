N = int(input())
A = list(map(int, input().split()))

ans = 0
tmp = 0
for a in A:
  ans += tmp * a
  tmp += a

print(ans)