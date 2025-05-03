from collections import deque

Q = int(input())

q = deque()
for _ in range(Q):
  query = input().split()
  
  if query[0] == '1':
    X = int(query[1])
    q.append(X)

  else:
    print(q.popleft())
