N, K = map(int, input().split())

if (N < K):
  print(1)
  exit()

A = [1] * (N + 1)
S = K
for i in range(K, N + 1):
  A[i] = S
  S = (S + A[i] - A[i - K]) % (10 ** 9)

print(A[N])