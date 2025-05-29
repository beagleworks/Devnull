N = int(input())
P = list(map(int, input().split()))

D = []
for i in range(1, N):
  if P[i] - P[i - 1] > 0:
    if len(D) > 0 and D[-1][0] == 1:
      D[-1][1] += 1
    else:
      D.append([1, 1])
  else:
    if len(D) > 0 and D[-1][0] == 1:
      D.append([-1, 0])

ans = 0
for i in range(len(D)):
  if i != len(D) - 1 and D[i][0] == -1:
    ans += D[i - 1][1] * D[i + 1][1]

print(ans)

