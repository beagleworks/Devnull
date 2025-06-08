T = input()
U = input()
n, m = len(T), len(U)

for i in range(n - m + 1):
    ok = True
    for j in range(m):
        if T[i + j] != '?' and T[i + j] != U[j]:
            ok = False
            break

    if ok:
        print("Yes")
        exit()

print("No")
