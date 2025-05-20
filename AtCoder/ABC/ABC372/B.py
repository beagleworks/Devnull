M = int(input())

ans = []
a = 10
while M > 0 and a >= 0:
  A = 3 ** a
  if M >= A:
    ans.append(a)
    M -= A
  else:
    a -= 1

print(len(ans))
print(*ans)