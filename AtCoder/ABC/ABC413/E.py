# クイックソートの要領で分割統治法でスワップするだけ
def solve():
    N = int(input())
    P = list(map(int, input().split()))

    s = 2
    while s <= (1 << N):
        t = s // 2
        for i in range(0, 1 << N, s):
            if P[i] > P[i + t]:
                for j in range(t):
                    k = i + j
                    P[k], P[k + t] = P[k + t], P[k]
        s *= 2
    
    print(*P)

def main():
    T = int(input())
    for _ in range(T):
        solve()

if __name__ == '__main__':
    main()