from collections import deque

N = int(input())
H = [10 ** 20] + list(map(int, input().split()))

q = deque()
prev = [0] * (N + 1)
for i in range(N + 1):
    while len(q) != 0 and q[-1][0] <= H[i]:
        q.pop()
    if len(q) > 0:
        prev[i] = q[-1][1]
    else:
        prev[i] = 0
    q.append((H[i], i))

dp = [0] * (N + 1)
for i in range(1, N + 1):
    dp[i] = dp[prev[i]] + H[i] * (i - prev[i])

ans = [x + 1 for x in dp]
ans.pop(0)
print(*ans)
