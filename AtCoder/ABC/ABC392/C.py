N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

R = [0] * N
for i in range(N):
    R[Q[i] - 1] = P[i] - 1

for i in range(N):
    print(Q[R[i]])
