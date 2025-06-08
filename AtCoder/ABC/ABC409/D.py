T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()

    idx = -1
    for i in range(N - 1):
        if S[i] > S[i + 1]:
            idx = i
            break

    if idx == -1:
        print(S)
        continue
    c = S[idx]
    b = S[idx + 1:]

    p = len(b)
    for k in range(1, len(b)):
        if b[k] > c:
            p = k
            break

    print(S[:idx] + b[:p] + c + b[p:])
