X = list(map(int, input().split()))
print("Yes" if X[0] > X[2] or (X[0] == X[2] and X[1] > X[3]) else "No")
