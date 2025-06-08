from collections import deque
import sys
input = sys.stdin.readline

Q = int(input())
q = deque()
head = 0
tail = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        q.append((tail, query[1]))
        tail += query[1]
    elif query[0] == 2:
        _, h = q.popleft()
        head += h
        if not q:
            tail = 0
            head = 0
    else:
        print(q[query[1] - 1][0] - head)
