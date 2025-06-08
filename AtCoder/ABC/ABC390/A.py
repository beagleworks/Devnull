A = list(map(int, input().split()))
for i in range(4):
    B = A[:]
    B[i], B[i + 1] = B[i + 1], B[i]
    if B == [1, 2, 3, 4, 5]:
        print("Yes")
        exit()

print("No")
