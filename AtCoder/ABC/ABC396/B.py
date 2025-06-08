from collections import deque

Q = int(input())
que = deque()

for _ in range(Q):
    line = input().split()
    if line[0] == '2':
        print(0 if not len(que) else que.popleft())
    else:
        que.appendleft(line[1])
