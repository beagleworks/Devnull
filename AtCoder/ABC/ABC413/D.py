# 項数2はYes
# Aの絶対値を昇順ソート(AA)
# AAが等比数列ではない→No
# AAの符号が全て一致→Yes
# AAの符号の数が半分ずつ、もしくはN:奇数で1つ差 を満たさない→No
# ここまででr = 1 →Yes
# r != 1で 実際に頭から調べて等比数列になっている→Yes
def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 2:
        print("Yes")
        return

    AA = sorted(abs(e) for e in A)
    for i in range(1, N - 1):
        if AA[i] * AA[i] != AA[i - 1] * AA[i + 1]:
            print("No")
            return

    pl = sum(1 for e in A if e > 0)
    if pl == 0 or pl == N:
        print("Yes")
        return

    if not (pl == N // 2 or (N % 2 and pl == N // 2 + 1)):
        print("No")
        return
    
    else:
        if AA[0] == AA[1]:
            print("Yes")
            return
        
        X = set(A)
        sign = -1
        for i in range(N):
            if i == 0:
                if AA[i] in X:
                    sign = 1
            else:
                sign *= -1
                if AA[i] * sign not in X:
                    print("No")
                    return       
    
    print("Yes")


def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()