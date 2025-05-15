from collections import deque

N = int(input())

P = [()] * (N * 2) 
for i in range(N):
  A, B = map(int, input().split())
  if A > B:
    A, B = B, A
  A -= 1
  B -= 1
  P[A] = (True, i)
  P[B] = (False, i)

q = deque()
for k in range(N * 2):
  if P[k][0]:
    q.append(P[k][1])
  else:
    if q[-1] != P[k][1]:
      print("Yes")
      exit()
    q.pop()

print("No")