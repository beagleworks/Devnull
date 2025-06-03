from sortedcontainers import SortedSet

N = int(input())
A = SortedSet(list(map(int, input().split())))

print(len(A))
print(*A)