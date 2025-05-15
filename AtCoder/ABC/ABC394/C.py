from collections import deque

S = input()
q = deque()

for s in S:
  if s != 'A':
    q.append(s)
  else:
    cnt = 0
    while len(q) > 0 and q[-1] == 'W':
      q.pop()
      cnt += 1
    q.extend(['A'] + ['C'] * cnt)    

print("".join(q))

