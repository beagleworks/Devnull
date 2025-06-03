X = int(input())
tmp = 1
for i in range(1, 21):
  tmp *= i
  if tmp == X:
    print(i)
    exit()