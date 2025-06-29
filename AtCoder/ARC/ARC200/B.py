import math
import sys

def main():
    input = sys.stdin.readline
    T = int(input())

    TEN = [1] * 19
    for i in range(1, 19):
        TEN[i] = TEN[i - 1] * 10

    ans = []
    for _ in range(T):
        A1, A2, A3 = map(int, input().split())
        M = max(A1, A2)
        # MAX(X1, X2) <= LCM(X1, X2) <= X1 * X2 より
        # A3桁はMの桁数以上、かつA1+A2桁を超えない
        if A3 < M or A3 > A1 + A2:
            ans.append("No")
            continue

        # A3 が A1 + A2 桁より小さいとき
        if A3 <= A1 + A2 - 1:
            U = A1 + A2 - A3 - 1
            X1U, X2U = A1 - U, A2 - U
            # ut, vt は互いに素
            ut = TEN[X1U - 1]
            vt = TEN[X2U - 1] + 1
            # LCM(X1, X2) = X1 * X2 / TEN[U](=GCD(X1, X2)
            # = ut * vt * TEN[U]
            X1, X2 = ut * TEN[U], vt * TEN[U]
            ans.append("Yes")
            ans.append(f"{X1} {X2}")
        # A3 が A1 + A2 桁のとき 
        else:
            # X1 は A1桁 の 9999...9
            X1 = TEN[A1] - 1
            # X2 は A2桁 の 9999...9 から 1, 2, ..., 9 を引いたものの中から
            # X1 と互いに素なものを探す
            X2 = 1
            for k in range(1, 10):
                X2 = TEN[A2] - k
                if math.gcd(X1, X2) == 1:
                    break
            ans.append("Yes")
            ans.append(f"{X1} {X2}")
    
    print("\n".join(ans))

if __name__ == '__main__':
    main()