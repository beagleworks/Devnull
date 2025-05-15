from collections import deque

N = int(input())
s = input()

q = deque()
for c in s:
  if c == 'x' and len(q) >= 2 and q[-1] == 'o' and q[-2] == 'f':
    q.pop()
    q.pop()
  else:
    q.append(c)

print(len(q))

