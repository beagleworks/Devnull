# 1. 相対順位の計算
# DFS で各連結成分内の制約を一度に解く。
# 2. ビットマスク表現
# 順位差集合をビットに落とし込み、シフトして配置可能性を調べる。
# 3. ビット DP
# ある成分だけ抜いて「他で埋められるか」を前計算。個別の成分を置ける位置が ちょうど１通り ならその成分内の頂点の順位は一意に確定。

def main():
    
    import sys
    sys.setrecursionlimit(10**7)
    
    N, M = map(int, input().split())
    Al = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        Al[a].append((b, -c))
        Al[b].append((a, c))
    
    taken = [False] * N
    idx = [0] * N # 各頂点の「任意原点からの相対順位」
    isle = [] # 連結成分ごとの頂点リスト
    bs = [] # 連結成分ごとのビットマスク

    # 連結成分ごとに処理
    for i in range(N):
        if taken[i]:
            continue
        isle.append([])
        # 辺の重みを足し合わせながらDFS
        def dfs(v):
            isle[-1].append(v)
            taken[v] = True
            for u, c in Al[v]:
                if not taken[u]:
                    idx[u] = idx[v] + c
                    dfs(u)
        
        dfs(i)

        # 連結成分ごとに最小 idx を引いて，順位差を [0, …, max] の範囲に正規化。
        # 1<<idx[v] を立てることで，成分全体の形状をビットマスク z として表現
        mn = min(idx[v] for v in isle[-1])
        for v in isle[-1]:
            idx[v] -= mn        
        z = 0
        for v in isle[-1]:
            z |= 1 << idx[v]
        bs.append(z)
    
    ans = [-1] * N
    K = len(bs)
    fm = (1 << N) - 1
    # ビットシフトを事前に計算しておく
    shifts = []
    for b in bs:
        max_bit = b.bit_length() - 1
        max_offset = N - max_bit
        shifts.append([b << s for s in range(max_offset)])
    
    for k in range(K):

        reachable = {0}
        for i in range(K):
            if i == k:
                continue
            nxt = set()
            for m in reachable:
                for s in shifts[i]:
                    if m & s == 0:
                        nxt.add(m | s)
            reachable = nxt
            if not reachable:
                break
        
        cnt = 0
        last_offset = -1
        for off, sk in enumerate(shifts[k]):
            comp = fm ^ sk
            if comp in reachable:
                cnt += 1
                last_offset = off

        if cnt == 1:
            for v in isle[k]:
                # 実際の順位(ans[v]) = (相対 idx[v]) + (成分シフト量) + 1
                ans[v] = idx[v] + last_offset + 1

    print(*ans)

if __name__ == '__main__':
    main()
