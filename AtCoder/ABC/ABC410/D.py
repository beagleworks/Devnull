# W の最大は 2^10 - 1 = 1023
# N(<=1000) * W(<=1023) 頂点のグラフを全探索すると考えればよい
def main():
    import sys
    input = sys.stdin.readline
    from collections import deque

    N, M = map(int, input().split())
    Adj = [[] for _ in range(N)]
    for _ in range(M):
        a, b, w = map(int, input().split())
        a -= 1
        b -= 1
        Adj[a].append((b, w))

    visited = [[False] * 1024 for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0)])
    while q:
        v, vw = q.popleft()
        for u, uw in Adj[v]:
            ww = vw ^ uw
            if not visited[u][ww]:
                visited[u][ww] = True
                q.append((u, ww))

    for i in range(1024):
        if visited[N - 1][i]:
            print(i)
            return

    print(-1)

if __name__ == '__main__':
    main()