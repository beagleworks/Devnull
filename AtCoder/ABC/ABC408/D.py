import sys
input = sys.stdin.readline

for _ in range(int(input())):
  input()
  S = input().strip()
  s1 = S.count('1')

  d = 0
  f = 0
  for c in S:
    v = 1 if c == '1' else -1
    d = max(0, d + v)
    f = max(f, d)

  print(s1 - f)