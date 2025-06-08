N = int(input())
S, T = input(), input()

ans = 0
for i in range(N):
    if S[i] != T[i]:
        ans += 1

print(ans)
