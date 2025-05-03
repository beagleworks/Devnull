N = int(input())

f = False
ans = 0
for _ in range(N):
  s = input()
  if s == "login":
    f = True
  elif s == "logout":
    f = False
  elif s == "private":
    ans += abs(f - 1)

print(ans)