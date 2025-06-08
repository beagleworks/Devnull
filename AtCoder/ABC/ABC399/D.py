import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    H = [[] for _ in range(N + 1)]
    for i in range(2 * N):
        H[A[i]].append(i)

    ans = set()

    for i in range(2 * N - 1):
        if H[A[i]][1] - H[A[i]][0] == 1 or H[A[i + 1]][1] - H[A[i + 1]][0] == 1:
            continue
        if H[A[i]][1] == i or H[A[i + 1]][1] == i + 1:
            continue

        if abs(H[A[i + 1]][1] - H[A[i]][1]) == 1:
            ans.add((A[i], A[i + 1]))

    print(len(ans))
