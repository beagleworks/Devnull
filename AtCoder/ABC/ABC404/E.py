N = int(input())
C = [0] + list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

ans = 0
for i in range(N - 1, 0, -1):
    if A[i] == 0:
        continue

    ans += 1
    ag = i
    tmp = 10 ** 30
    for j in range(i - 1, i - C[i] - 1, -1):
        if A[j] > 0 or j == 0:
            A[i] = 0
            break

        if tmp > j - C[j]:
            tmp = j - C[j]
            ag = j

    if A[i] != 0:
        A[ag] = 1
        A[i] = 0

print(ans)
