N, M = map(int, input().split())
A = list(map(int, input().split()))

seen = set()
L = -1
for i, a in enumerate(A, 1):
    seen.add(a)
    if len(seen) == M:
        L = i
        break

print(0 if L == -1 else N - L + 1)
