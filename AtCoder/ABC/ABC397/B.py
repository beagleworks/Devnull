S = input()

ans = 0
for i in range(len(S)):
    if ((i + ans) %
        2 == 0 and S[i] == 'o') or ((i + ans) %
                                    2 == 1 and S[i] == 'i'):
        ans += 1
        i -= 1

if (len(S) + ans) % 2 == 1:
    ans += 1
print(ans)
