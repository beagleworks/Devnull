from collections import deque

N = int(input())
A = list(map(int, input().split()))

q = deque()

ans = 0
for a in A:
    if len(q) == 0 or q[-1][0] != a:
        q.append([a, 1])
        ans += 1
    else:
        q[-1][1] += 1
        ans += 1
        if q[-1][1] == q[-1][0]:
            q.pop()
            ans -= a

    print(ans)
