from collections import deque

S = input()

q = deque()
for s in S:
    if len(q) > 0 and ((q[-1] == '(' and s == ')') or (q[-1]
                                                       == '<' and s == '>') or (q[-1] == '[' and s == ']')):
        q.pop()
    else:
        q.append(s)

print("Yes" if len(q) == 0 else "No")
