import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
G = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, w))

ans = 0

st = [(0, -1, 0)]
while st:
    pt, pre, state = st.pop()
    if state == 0:
        st.append((pt, pre, 1))
        for nei, w in G[pt]:
            if nei == pre:
                continue
            st.append((nei, pt, 0))
    else:
        for nei, w in G[pt]:
            if nei == pre:
                continue

            s = X[nei]
            ans += abs(s) * w
            X[pt] += s

print(ans)
