import sys
input = sys.stdin.readline

N, M = map(int, input().split())
fqu = [0] * N
pal = 0

for _ in range(M):
  a, b = map(int, input().split())
  x = (a + b) % N

  pal += fqu[x]
  fqu[x] += 1

print((M * (M - 1) // 2) - pal)
