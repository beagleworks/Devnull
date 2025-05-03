N, K = map(int, input().split())
S = input()

need = K - S.count('o')
free = [False] * N
for i, ch in enumerate(S):
  if ch == '?':
    ok = True
    if i - 1 >= 0 and S[i - 1] == 'o':
      ok = False
    if i + 1 < N and S[i + 1] == 'o':
      ok = False
    free[i] = ok

seg_starts = []
seg_ends = []
seg_max = []

i = 0
while i < N:
  if free[i]:
    start = i
    while i + 1 < N and free[i + 1]:
      i += 1
    end = i
    seg_starts.append(start)
    seg_ends.append(end)
    L = end - start + 1
    seg_max.append((L + 1) // 2)
  i += 1

total_max = sum(seg_max)
J = len(seg_starts)
global_min = [0] * J
global_max = [0] * J

for j in range(J):
  mj = seg_max[j]
  gm = need - (total_max - mj)
  if gm < 0:
    gm = 0
  global_min[j] = gm
  global_max[j] = mj if mj < need else need

seg_index = [-1] * N
for j in range(J):
  s, e = seg_starts[j], seg_ends[j]
  for k in range(s, e + 1):
    seg_index[k] = j

T = [''] * N
for i in range(N):
  ch = S[i]
  if ch == 'o':
    T[i] = 'o'
  elif ch == '.':
    T[i] = '.'
  elif not free[i]:
    T[i] = '.'
  else:
    j = seg_index[i]
    start, end = seg_starts[j], seg_ends[j]
    L = end - start + 1
    p = i - start

    gm = global_min[j]
    gM = global_max[j]

    max_left  = p // 2
    max_right = (L - p - 1) // 2
    inc_max   = 1 + max_left + max_right
    inc_possible = (need >= 1 and gM >= 1 and gm <= inc_max)

    exc_max       = ((p + 1) // 2) + ((L - p) // 2)
    exc_possible  = (gm <= exc_max)

    if inc_possible and not exc_possible:
      T[i] = 'o'
    elif exc_possible and not inc_possible:
      T[i] = '.'
    else:
      T[i] = '?'

print(''.join(T))