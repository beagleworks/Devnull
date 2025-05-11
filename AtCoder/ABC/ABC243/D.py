from collections import deque

N, X = map(int, input().split())
S = input()

q = deque()
for s in S:
  if s == 'U' and len(q) > 0 and q[-1] != 'U':
    q.pop()
  else:
    q.append(s)

ans = X
while len(q) > 0:
  s = q.popleft()
  if s == 'U':
    ans //= 2
  else:
    ans *= 2
    ans += 1 if s == 'R' else 0

print(ans)
