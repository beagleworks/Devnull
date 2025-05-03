from collections import defaultdict

_, M = map(int, input().split())

x = defaultdict(list)
nbadfoods = [0] * M

for i in range(M):
  line = list(map(int, input().split()))
  foods = line[1:]
  for fi in foods:
    fi -= 1
    x[fi].append(i)
    nbadfoods[i] += 1

B = list(map(int, input().split()))
B = [b - 1 for b in B]

ans = 0
for b in B:
  for fd in x[b]:
    nbadfoods[fd] -= 1
    if nbadfoods[fd] == 0:
      ans += 1
  print(ans)
