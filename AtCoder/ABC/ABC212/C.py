from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))

ans = 10 ** 10
for a in A:
    idx = bisect_left(B, a)
    if 0 < idx < len(B):
        ans = min(ans, abs(a - B[idx]), abs(a - B[idx - 1]))
    elif idx == 0:
        ans = min(ans, abs(a - B[idx]))
    elif idx == len(B):
        ans = min(ans, abs(a - B[idx - 1]))

print(ans)