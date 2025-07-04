# A, B の各要素について、初めて出現する位置を格納(Ao, Bo)
# A, B の各要素について、それがB, Aのどの位置に初めて出現するかを取得し、それまでの累積の最大値を格納しておく(Ai, Bi)
# 各x, yについて、初めて出現する位置以下であればよい

def main():
    import sys
    input = sys.stdin.readline
    
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))    
    
    Ao = {}
    Bo = {}
    for i in range(N):
        a = A[i]
        if a not in Ao:
            Ao[a] = i
        b = B[i]
        if b not in Bo:
            Bo[b] = i

    INF = 10 ** 8
    Ai = [INF] * N
    Bi = [INF] * N
    for i in range(N):
        a = A[i]
        b = B[i]
        if a in Bo:
            Ai[i] = Bo[a]
        if b in Ao:
            Bi[i] = Ao[b]

    for i in range(1, N):
        Ai[i] = max(Ai[i], Ai[i - 1])
        Bi[i] = max(Bi[i], Bi[i - 1])

    Q = int(input())
    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1

        if Ai[x] <= y and Bi[y] <= x:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()