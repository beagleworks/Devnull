# https://qiita.com/drken/items/97e37dd6143e33a64c8c
# めぐる式二分探索

S = range(100)
left = -1
right = len(S)
while right - left > 1:
    mid = left + (right - left) // 2
    # 条件を満たすもの
    if True:
        left = mid
        # もしくはright = mid
    else:
        right = mid
        # left = mid