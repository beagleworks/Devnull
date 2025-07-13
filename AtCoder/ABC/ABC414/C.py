def main():
    A = int(input())
    N = int(input())

    # x(10進数) を A進数に直したとき、それが回文になっているかを判定する
    def judge(x, A):
        tmp = []
        while x:
            tmp.append(x % A)
            x //= A
        return tmp == tmp[::-1]
    
    ans = 0
    for k in range(1, 10 ** 6 + 1):
        sk = str(k)
        C1 = int(sk + sk[::-1])
        C2 = int(sk + sk[::-1][1:])

        if C1 <= N and judge(C1, A):
            ans += C1
        if C2 <= N and judge(C2, A):
            ans += C2
        if C2 > N:
            break

    print(ans)

if __name__ == "__main__":
    main()