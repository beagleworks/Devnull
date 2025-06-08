import sys
input = sys.stdin.readline

N, L = map(int, input().split())
D = list(map(int, input().split()))

if L % 3 != 0:
    print(0)
    sys.exit()

T = L // 3
pos = [0] * N
for i in range(1, N):
    pos[i] = (pos[i - 1] + D[i - 1]) % L
cnt = [0] * L
for p in pos:
    cnt[p] += 1

ans = 0
for t in range(T):
    ans += cnt[t] * cnt[t + T] * cnt[t + 2 * T]

print(ans)
