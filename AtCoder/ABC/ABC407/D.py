H, W = map(int, input().split())
N = H * W
A = []

for _ in range(H):
  A.extend(map(int, input().split()))

K = [[] for _ in range(N)]
for i in range(H):
  for j in range(W):
    u = i * W + j
    if j + 1 < W:
      K[u].append(u + 1)
    if i + 1 < H:
      K[u].append(u + W)

# 有効な配置かどうか
dp = [False] * (1 << N)
dp[0] = True

# ドミノを置いたマスの各パターンについて、XORの和を格納しておくxorv
xorv = [0] * (1 << N)

# 全てのマスのXORを事前に計算しておく
tot = 0
for v in A:
  tot ^= v
ans = tot

# tot^xorv = 空きマスのXORの和 となるため
# 最大になるものが答え

for b in range(1, 1 << N):
  lb = b & -b
  i = lb.bit_length() - 1
  prev = b ^ lb
  xorv[b] = xorv[prev] ^ A[i]
  for j in K[i]:
    if prev >> j & 1 and dp[prev ^ (1 << j)]:
      dp[b] = True
      break
  if dp[b]:
    ans = max(ans, tot ^ xorv[b])

print(ans)