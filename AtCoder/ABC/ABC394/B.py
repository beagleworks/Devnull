N = int(input())

W = []
for _ in range(N):
  S = input()
  W.append((len(S), S))

W.sort()
print(''.join(s for _, s in W))