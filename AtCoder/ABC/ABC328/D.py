from collections import deque

S = input()

q = deque()
for s in S:
    if s == 'C':
        if len(q) >= 2 and q[-1] == 'B' and q[-2] == 'A':
            q.pop()
            q.pop()
        else:
            q.append(s)
    else:
        q.append(s)

print("".join(list(q)))
