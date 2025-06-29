# ラグランジュ補間で分母を求めるとO(p^3)となり間に合わない
# ウィルソンの定理を利用してO(p^2)へと計算量を落とす
def main():
    p = int(input())
    A = list(map(int, input().split()))

    S = [0] * p
    powj = [1] * p
    # S[i] = ΣA[j] * j^i (mod p)
    for i in range(p):
        sm = 0
        for j in range(p):
            sm += A[j] * powj[j]
        S[i] = sm % p
        # 更新
        for k in range(p):
            powj[k] = (powj[k] * k) % p
    
    ans = [0] * p
    ans[0] = (S[0] - S[-1] + p) % p
    for i in range(1, p):
        ans[i] = (p - S[p - 1 - i]) % p
    
    print(*ans)

if __name__ == '__main__':
    main()