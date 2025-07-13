# 長方形[ ]に対して [|-] のように切り取るパターン(D2_1) と [||]のように切り取るパターン(D2_2)を、ABCの順列全通り分試す
# X, Yを入れ替え、全通り試す

def main():
    from itertools import permutations

    X, Y, A, B, C = map(int, input().split())

    T = list(permutations([A, B, C], 3))
    def edge_ceil(x, y):
        return (x + y - 1) // y

    for i in range(2):
        for t in T:
            D1 = edge_ceil(t[0], Y)
            if D1 >= X:
                continue

            D2_1 = edge_ceil(t[1], X - D1)
            if D2_1 < Y:
                if (X - D1) * (Y - D2_1) >= t[2]:
                    print("Yes")
                    return
            
            D2_2 = edge_ceil(t[1], Y)
            if D1 + D2_2 < X:
                if (X - D1 - D2_2) * Y >= t[2]:
                    print("Yes")
                    return

        X, Y = Y, X

    print("No")

 
if __name__ == '__main__':
    main()