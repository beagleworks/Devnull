from collections import deque

N = int(input())
A = list(map(int, input().split()))

q = deque()


def queuePush(x, q: deque):
    n = x
    while len(q) > 0:
        if q[-1] == n:
            n = q.pop() + 1
        else:
            break
    q.append(n)
    return q


for i in range(N):
    q = queuePush(A[i], q)

print(len(q))
