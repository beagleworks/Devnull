import sys
input = sys.stdin.readline

N, X = map(int, input().split())
n1 = 1 << N
S = [0] * N
C = [0] * N
p = [0.0] * N

for i in range(N):
    S[i], C[i], tp = map(int, input().split())
    p[i] = tp / 100.0

act = [[] for _ in range(n1)]
for mask in range(n1):
    for i in range(N):
        if not (mask >> i) & 1:
            act[mask].append((C[i], p[i], S[i], mask | (1 << i)))

dp = [[0.0] * (X + 1) for _ in range(n1)]
tmp = sorted(range(n1), key=lambda m: bin(m).count('1'), reverse=True)

for mask in tmp:
    fmask = dp[mask]
    for j in range(X + 1):
        nowbest = 0.0
        for cost, prob, score, next_mask in act[mask]:
            if cost <= j:
                v = prob * (score + dp[next_mask][j - cost]
                            ) + (1 - prob) * fmask[j - cost]
                if v > nowbest:
                    nowbest = v
        fmask[j] = nowbest

print(dp[0][X])
