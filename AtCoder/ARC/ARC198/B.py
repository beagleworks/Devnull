import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  X, Y, Z = map(int, input().split())

  # "0"の間に"2"が配置できるように、X >= Z が条件
  if X < Z:
    print("No")
    continue

  # "0"の間に"1"「のみ」を配置したときに、残る"1"の数
  rest_one = max(0, Y - 2 * (X - Z))
  # "0 - 2 - 0"の間に配置できる"1"の実際の数(=> 0 - 1 - 2 - 1 - 0)
  capa_one = min(Y, 2 * Z)
  if rest_one > capa_one:
    print("No")
    continue
  
  # 偶奇性のチェック
  # 合わないときは残った"1"を一つ増やす
  # 意味的には "0 - 1 - 2 - 0" のような組み合わせを作る
  if (rest_one & 1) != (Y & 1):
    rest_one += 1
  print("Yes" if rest_one <= capa_one else "No")