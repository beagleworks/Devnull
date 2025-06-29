X = input()

ans = 0
for i in range(3):
    if (int(X[i]) + 1) % 10 != int(X[i + 1]):
        ans = 1
        break

if all(x == X[0] for x in X):
    ans = 0

print("Strong" if ans else "Weak")



