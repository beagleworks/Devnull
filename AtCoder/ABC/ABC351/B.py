N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]

for i in range(N):
    for j in range(N):
        if A[i][j] != B[i][j]:
            print(i + 1, j + 1)
