N, M = map(int, input().split())
Rn = list(tuple(map(int, input().split())) for _ in range(M))
E = [0] * (N + 1)
for r in Rn:
  E[r[0] - 1] += 1
  E[r[1]] -= 1

for i in range(1, N):
  E[i] += E[i - 1]

E.pop()
print(min(E))