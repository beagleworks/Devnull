from collections import deque

N = int(input())
S = input()

t = S.find('(')
if t == -1:
  print(S)
  exit()

ans = S[:t]
S = S[t:]
q = deque()

for s in S:
  if s == '(':
    q.append('(')
  elif len(q) == 0:
    ans += s
  elif 'a' <= s <= 'z':
    q[-1] += s
  else:
    q.pop()

print(ans + ''.join(q))

