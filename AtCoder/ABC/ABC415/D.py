# 交換回数を最大化する方法を考える問題
# 交換の際最も元手が減らない(a-bが最少)ものから順に交換を試す

def main():
    N, M = map(int, input().split())
    C = []
    for _ in range(M):
        a, b = map(int, input().split())
        C.append((a - b, a))
    
    C.sort()
    tmp = N
    ans = 0
    for i in range(M):
        if tmp >= C[i][1]:
            a = 1 + (tmp - C[i][1]) // C[i][0]
            ans += a
            tmp -= a * C[i][0]
    
    print(ans)

if __name__ == '__main__':
    main()