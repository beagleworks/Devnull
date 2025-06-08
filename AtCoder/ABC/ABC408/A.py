N, S = map(int, input().split())
A = list(map(int, input().split()))

tmp = 0
for a in A:
    if a - tmp > S:
        print("No")
        exit()
    tmp = a

print("Yes")
