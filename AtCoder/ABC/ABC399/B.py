from bisect import bisect_right

N = int(input())
P = list(map(int, input().split()))
Q = sorted(P)

for p in P:
    print(N - bisect_right(Q, p) + 1)
