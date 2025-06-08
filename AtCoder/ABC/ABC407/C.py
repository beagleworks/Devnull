S = input()
ans = 0
bcnt = 0

for i in range(len(S) - 1, -1, -1):
    n = (int(S[i]) - bcnt) % 10
    now = n % 10
    bcnt += now
    ans += now + 1

print(ans)
