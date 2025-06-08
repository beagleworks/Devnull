N = int(input())
A = list(map(int, input().split()))

for x in range(N, -1, -1):
    cnt = sum(a >= x for a in A)
    if cnt >= x:
        print(x)
        break
