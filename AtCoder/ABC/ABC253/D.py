# 1~Nの和 - 1~NにおけるAの倍数の和 - 1~NにおけるBの倍数の和 + 1~NにおけるCの倍数の和
# ただしCはAとBの最小公倍数
def main():
    import math

    N, A, B = map(int, input().split())
    C = math.lcm(A, B) 
    print(N * (N + 1) // 2 - A * (N // A) * (N // A + 1) // 2 - B * (N // B) * (N // B + 1) // 2 + C * (N // C) * (N // C + 1) // 2)

if __name__ == '__main__':
    main()