MOD = 998244353
P2 = [1] * 61
for i in range(1, 61):
  P2[i] = P2[i - 1] * 2 % MOD

T = int(input())
for _ in range(T):
  N, K = map(int, input().split())

  bits = []
  tmp = N
  while tmp > 0:
    bits.append(tmp & 1)
    tmp >>= 1
  L = len(bits)
  bits = bits[::-1]

  dpn = [[0, 0] for _ in range(K + 2)]
  dpa = [[0, 0] for _ in range(K + 2)]
  dpn[0][1] = 1
  dpa[0][1] = 0

  for l in range(L):
    t_dpn = [[0, 0] for _ in range(K + 2)]
    t_dpa = [[0, 0] for _ in range(K + 2)]
    for k in range(K + 1):
      c0, c1 = dpn[k]
      s0, s1 = dpa[k]

      if c0:
        t_dpn[k][0] = (t_dpn[k][0] + c0) % MOD
        t_dpa[k][0] = (t_dpa[k][0] + s0) % MOD
        if k + 1 <= K:
          t_dpn[k + 1][0] = (t_dpn[k + 1][0] + c0) % MOD
          t_dpa[k + 1][0] = (t_dpa[k + 1][0] + s0 + c0 * P2[L - 1 - l]) % MOD

      if c1:
        if bits[l] == 0:
          t_dpn[k][1] = (t_dpn[k][1] + c1) % MOD
          t_dpa[k][1] = (t_dpa[k][1] + s1) % MOD
        else:
          t_dpn[k][0] = (t_dpn[k][0] + c1) % MOD
          t_dpa[k][0] = (t_dpa[k][0] + s1) % MOD
          if k + 1 <= K:
            t_dpn[k + 1][1] = (t_dpn[k + 1][1] + c1) % MOD
            t_dpa[k + 1][1] = (t_dpa[k + 1][1] + s1 + c1 * P2[L - 1 - l]) % MOD

    dpn = t_dpn
    dpa = t_dpa

  ans = (dpa[K][0] + dpa[K][1]) % MOD
  print(ans)