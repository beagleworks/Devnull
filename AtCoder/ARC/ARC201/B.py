# 品物を重さで分類する
# 各重さ区分(各bit)について、選ぶ品物の数は高々1個(当該bitが立っているか否か)
# 選ばれなかった品物は、2つ合わせて1つ上の区分に組み込む。1つだけ残った品物もそのまま上の区分に。
def solve():
    import sys
    input = sys.stdin.readline
    import heapq

    N, W = map(int, input().split())
    X, Y = zip(*(map(int, input().split()) for _ in range(N)))
    X, Y = list(X), list(Y)

    PriceList = [[] for _ in range(62)]
    for i in range(N):
        heapq.heappush(PriceList[X[i]], -Y[i])
    
    ans = 0
    for i in range(61):
        if W & (1 << i) and PriceList[i]:
            ans += (-1) * heapq.heappop(PriceList[i])
        
        # 2個組み合わせて、重さ2倍で価値a1+a2のものをつくる
        while len(PriceList[i]) > 1:
            a1 = heapq.heappop(PriceList[i])
            a2 = heapq.heappop(PriceList[i])
            heapq.heappush(PriceList[i + 1], a1 + a2)
        
        # 1個だけ残ったときはそのまま重さを2倍
        if PriceList[i]:
            heapq.heappush(PriceList[i + 1], heapq.heappop(PriceList[i]))
        
    print(ans)
    return    

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()
