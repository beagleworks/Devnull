N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Aの要素の和とBの要素の和が等しくないとダメ
if sum(A) != sum(B):
    print("No")
    exit()

# N = 2はエッジケース
# 0回、もしくは1回の操作で一致しないとNo
if N == 2:
    if A == B:
        print("Yes")
        print(0)
        exit()
    if B == [A[1] - 1, A[0] + 1]:
        print("Yes")
        print(1)
        print(1, 2)
    else:
        print("No")
    exit()

ans = []
# 要素の交換を記録する
# 対象要素が端にある場合は別途処理


def swap(i, j):
    # 交換要素が両端
    if i == 0 and j == N - 1:
        ans.append((1, N))
        ans.append((1, 2))
        ans.append((2, N))
        ans.append((1, 2))
        ans.append((1, N))
    # 左の要素が左端のとき
    elif i == 0:
        ans.append((j + 1, N))
        ans.append((1, N))
        ans.append((j + 1, N))
    else:
        ans.append((1, j + 1))
        ans.append((1, i + 1))
        ans.append((1, j + 1))


# 左から順に見ていく
# Ai < Bi かつ Aj > Bj もしくは Ai > Bi かつ Aj < Bj の組を探して交換する
# j側の要素が先に等しくなったら、そのjの先から残りの交換要員を探す
for i in range(N):
    if A[i] == B[i]:
        continue

    for j in range(i + 1, N):
        if A[i] < B[i] and A[j] > B[j]:
            cnt = min(B[i] - A[i], A[j] - B[j])
            A[i] += cnt
            A[j] -= cnt
            for _ in range(cnt):
                ans.append((i + 1, j + 1))
                swap(i, j)
        elif A[i] > B[i] and A[j] < B[j]:
            cnt = min(A[i] - B[i], B[j] - A[j])
            A[i] -= cnt
            A[j] += cnt
            for _ in range(cnt):
                swap(i, j)
                ans.append((i + 1, j + 1))

        if A[i] == B[i]:
            break

print("Yes")
print(len(ans))
for i, j in ans:
    print(i, j)
