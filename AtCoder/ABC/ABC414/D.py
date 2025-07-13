# 全体を1台の基地局で網羅すると考えてから、最長距離間隔の部分をカットしていく
def main():
    N, M = map(int, input().split())
    X = sorted(list(map(int, input().split())))

    if M == N:
        print(0)
        return

    D = [X[i + 1] - X[i] for i in range(N - 1)]
    D.sort()
    
    ans = X[-1] - X[0] - (sum(D[-(M - 1):]) if M - 1 > 0 else 0)
    print(ans)

if __name__ == "__main__":
    main()
