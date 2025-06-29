# Div1の開催上限、Div2の開催上限、Mediumの均等分配のうち最も弱いものが答え
# ans = Min(Div1, Div2, H // 2)

def main():
    import sys
    input = sys.stdin.readline

    T = int(input())
    for _ in range(T):
        N = int(input())
        D1, D2, H = 0, 0, 0
        for _ in range(N):
            A, B, C = map(int, input().split())
            D1 += min(A, B)
            D2 += min(C, B)
            H += min(A + C, B)

        ans = min(D1, D2, H // 2)
        print(ans)

if __name__ == '__main__':
    main()
