from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

L = defaultdict(int)
R = defaultdict(int)

for a in A:
    L[a] += 1

LS = set(A)
RS = set()

ans = len(LS) + len(RS)

for i in range(N):
    a = A[i]
    R[a] += 1
    L[a] -= 1
    if L[a] == 0:
        LS.remove(a)
    RS.add(a)
    ans = max(ans, len(LS) + len(RS))

print(ans)
