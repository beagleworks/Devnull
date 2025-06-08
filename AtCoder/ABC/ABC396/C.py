N, M = map(int, input().split())
B = sorted(list(map(int, input().split())), reverse=True)
W = sorted(list(map(int, input().split())), reverse=True)

ans = 0
for i in range(N):
  if B[i] >= 0:
    ans += B[i]
    if i < M:
      ans += max(0, W[i])
  elif i < M:
    if B[i] + W[i] >= 0:
      ans += B[i] + W[i]
  else:
    break

print(ans)
