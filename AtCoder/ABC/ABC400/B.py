N, M = map(int, input().split())

if N == 1:
  print(M + 1)
else:
  ans = (N ** (M + 1) - 1)  // (N - 1)
  print("inf" if ans > 10 ** 9 else str(ans))

