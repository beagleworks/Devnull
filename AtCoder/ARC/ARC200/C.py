import heapq
import sys

# 逆順にトポロジカルソートっぽいのを行い、席番号を割り当てる

def main():
    input = sys.stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        lines = [tuple(map(int, input().split())) for _ in range(N)]

        adj = [[] for _ in range(N)]
        rev_adj = [[] for _ in range(N)]
        dgr = [0] * N

        for i in range(N):
            for j in range(i + 1, N):
                li, ri = lines[i]
                lj, rj = lines[j]
                
                if li < lj and rj < ri:
                    adj[j].append(i)
                    rev_adj[i].append(j)
                    dgr[j] += 1

                elif lj < li and ri < rj:
                    adj[i].append(j)
                    rev_adj[j].append(i)
                    dgr[i] += 1

        CHP = []
        for i in range(N):
            if dgr[i] == 0:
                heapq.heappush(CHP, -i)
        
        ans = [0] * N
        # k は席番号
        for k in range(N, 0, -1):
            if not CHP:
                break
                
            u = -heapq.heappop(CHP)

            ans[u] = k
            
            for v in rev_adj[u]:
                dgr[v] -= 1
                if dgr[v] == 0:
                    heapq.heappush(CHP, -v)
                    
        print(*ans)

if __name__ == "__main__":
    main()