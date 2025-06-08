from fractions import Fraction

N = int(input())
A = list(map(int, input().split()))

r = Fraction(A[1], A[0])

for i in range(N - 1):
    if A[i] * r != A[i + 1]:
        print("No")
        exit()

print("Yes")
